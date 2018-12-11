#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
update on 2018-5-10
'''
import MySQLdb as mdb
import rospy
from neu_wgg.msg import env_and_angle
import sys
import time
import thread

#环境信息
atmo=0
temp=0
hum=0
#关节角度信息
leftk=0
lefth=0
rightk=0
righth=0
num=0
longitude=0
latitude=0
count = 0
class Storage:
    def __init__(self):
        topic_name = "store_topic_"+exo_id
        rospy.Subscriber(topic_name,env_and_angle,self.callback)
        self.conn_exo=mdb.connect(host="127.0.0.1",user="root",db="NeuExo",passwd="ubuntu",charset="utf8")
        self.conn_exo.ping(True)
        self.cur_exo=self.conn_exo.cursor()
        self.data = (0,0,0,0,0,0,0,0,0)
        # thread.start_new_thread(self.LogExoID,())
    def callback(self,data):
        self.atmo = data.atmo
        self.hum = data.hum
        self.temp = data.temp
        self.leftk=data.leftk
        self.lefth=data.lefth
        self.rightk=data.rightk
        self.righth=data.righth
        self.longitude=data.longitude
        self.latitude=data.latitude
        self.data=(self.leftk,self.lefth,self.rightk,self.righth,self.temp,self.hum,self.atmo,self.longitude,self.latitude)
        self.UpdateExoSum()
        # self.LogExoID()
#将关节角度和环境数据以及地理位置信息存放到数据库
    def UpdateExoSum(self):
        self.cur_exo.execute("update exo_sum set leftk=%s,lefth=%s,rightk=%s,righth=%s,temp=%s,hum=%s,atmo=%s,longitude=%s,"
                    "latitude=%s where id="+exo_id, (self.leftk,self.lefth,self.rightk,self.righth,self.temp,self.hum,
                                            self.atmo,self.longitude,self.latitude))
        self.conn_exo.commit()
#将关节角度和环境数据的历史数据存放到相对应的数据库
    def LogExoID(self):
        # while 1:
            # time_stamp = time.asctime( time.localtime(time.time()) )
            # time_tuple=(time_stamp,)
            global count
            count = count + 1
            count_tuple = (count,)
            log_data=count_tuple+self.data
            self.cur_exo.execute("insert into exo_"+exo_id+" values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",log_data)
            time.sleep(2)
            self.conn_exo.commit()
if __name__=="__main__":
    exo_id = sys.argv[1]
    rospy.init_node("store",anonymous = True)
    Storage()
    rospy.spin()
