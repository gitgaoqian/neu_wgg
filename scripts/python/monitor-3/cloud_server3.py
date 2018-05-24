#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import os
import sys
import thread
import MySQLdb as mdb
import IPy

# Add custom service here
app = flask.Flask(__name__)

if "CLOUD_IP" not in os.environ:
    print
    "Can't find environment variable CLOUD_IP."
    sys.exit(1)
cloud_ip = os.environ['CLOUD_IP']
port = 5566
class NeuExo():
    def __init__(self):
        self.conn = mdb.connect(host="127.0.0.1", user="root", db="NeuExo", passwd="ubuntu", charset="utf8")
        self.cur = self.conn.cursor()
        # threaded = True:开启app路由多线程并发,可以同时处理多个http请求，即路由函数可以同时执行
        # threaded = False:开启app路由单线程，一次只能处理一个http请求
        #路由uri
        @app.route('/storage/<robotID>/<action>',methods=['POST'])
        def ServiceHandler(robotID,action):
            token = flask.request.remote_addr
            is_auth = self.IsAuth(token)  # 首先进行身份验证
            if not is_auth:  # 验证失败
                return "Auth failed,the exo/monitor has no access to the cloud"
            self.ROSNetworkConfig()
            if action == "store":
                is_exo = self.IsExoInExoSum(robotID)  # 查看ExoSum中有没有请求的Exo
                if not is_exo:  # 如果没有,创建表,并将该Exo信息插入到ExoSum中
                    self.CreateExoID(robotID)
                    self.InsertExoSum(robotID)
                else:  # 如果ExoSum中有Exo信息,首先清空ExoID的旧的历史数据,然后进行新的数据存储
                    self.ClearExoID(robotID)
                thread.start_new_thread(self.StoreData, (robotID,))
                return "Store Exo_" + robotID + " data"
            elif action == "fetch":
                is_exo = self.IsExoInExoSum(robotID)
                if not is_exo:
                    return "No table exo" + str(robotID) + " for fetch"
                else:
                    thread.start_new_thread(self.FetchData, (robotID,))
                    return "Fetch Exo_" + robotID + " data"
            else:
                return action + " not permitted! for monitor,action=fetch;for exo,action=store"
        # 运行云端服务器
        # 注:app.run和app.route执行的前后顺序似乎只能是app.run在app.route之后执行
        app.run(host=cloud_ip, port=port, threaded=True)
    def IsAuth(self,token):
        # 此处设置token为ip,判断ip处于的子网段是否在数据库NeuExo的token表中
        subnet = str((IPy.IP(token).make_net('255.255.255.0')))#找到ip在的网段ex:192.168.1.0/24
        rows = self.cur.execute("select * from token where token=%s", subnet)
        if rows == 0:
            return False
        else:
            return True
    def IsExoInExoSum(self, robotID):
        rows = self.cur.execute("select * from exo_sum where id=%s", (robotID))
        if rows == 0:
            return False
        else:
            return True
    def InsertExoSum(self, robotID):
        self.cur.execute("insert into exo_sum values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (robotID,None,None,None,None,
                                                                                        None,None,None,None,None))
        self.conn.commit()
    def CreateExoID(self,robotID):
        self.cur.execute("create table exo_"+str(robotID)+" (count int,leftk float,lefth float,"
                                                         "rightk float,righth float,temp float,hum float,"
                                                         "atmo float,longitude float,latitude float)")
    def ClearExoID(self,robotID):
        self.cur.execute("truncate table exo_"+robotID)
        self.conn.commit()
    def StoreAndFetch(self,robotID,action):
        if action == "store":
            is_exo = self.IsExoInExoSum(robotID)  # 查看ExoSum中有没有请求的Exo
            if not is_exo:  # 如果没有,创建表,并将该Exo信息插入到ExoSum中
                self.CreateExoID(robotID)
                self.InsertExoSum(robotID)
            else:  # 如果ExoSum中有Exo信息,首先清空ExoID的旧的历史数据,然后进行新的数据存储
                self.ClearExoID(robotID)
            thread.start_new_thread(self.StoreData, (robotID,))
            return "Store Exo_" + robotID + " data"
        elif action == "fetch":
            is_exo = self.IsExoInExoSum(robotID)
            if not is_exo:
                return "No table exo" + str(robotID) + " for fetch"
            else:
                thread.start_new_thread(self.FetchData, (robotID,))
                return "Fetch Exo_" + robotID + " data"
        else:
            return action + " not permitted! for monitor,action=fetch;for exo,action=store"
    def ROSNetworkConfig(self):
        ros_master_ip = flask.request.remote_addr
        ros_master_uri = 'http://' + ros_master_ip + ':11311'
        os.environ['ROS_MASTER_URI'] = ros_master_uri
        os.environ['ROS_IP'] = cloud_ip
    def StoreData(self, robotID):
        os.system('rosrun neu_wgg store_service.py '+robotID+" __name:=StoreService"+robotID)
    def FetchData(self, robotID):
        os.system('rosrun neu_wgg fetch_service.py ' + robotID+" __name:=FetchService"+robotID)
if __name__ == '__main__':
    NeuExo()

