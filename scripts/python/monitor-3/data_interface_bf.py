#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import rospy
from neu_wgg.msg import env_and_angle
import sys  
import time

#环境信息
atmo=0
temp=0
hum=0
#关节角度信息
leftk=0
lefth=0
rightk=0
righth=0
exo_id=0
num=0
longitude=0
latitude=0

class Data_Interface:
    def __init__(self):
        rospy.Subscriber('env_and_angle',env_and_angle,self.callback) 
        self.conn_exo=mdb.connect(host="127.0.0.1",user="root",db="exo1213",passwd="ubuntu",charset="utf8")
        self.cur_exo=self.conn_exo.cursor()
        self.conn_exolog=mdb.connect(host="127.0.0.1",user="root",db="exo_"+exo_id,passwd="ubuntu",charset="utf8")
        self.cur_exolog=self.conn_exolog.cursor()
    def callback(self,data):
        global leftk
        global lefth
        global rightk
        global righth
        global atmo
        global temp
        global hum
        global longitude
        global latitude
        atmo = data.atmo
        hum = data.hum
        temp = data.temp
        leftk=data.leftk
        lefth=data.lefth
        rightk=data.rightk
        righth=data.righth
        longitude=data.longitude
        latitude=data.latitude
        data=(leftk,lefth,rightk,righth,temp,hum,atmo,longitude,latitude)
        self.update_exo(data)
        self.exo_log(data)
#将关节角度和环境数据存放到数据库
    def update_exo(self,data):
        self.cur_exo.execute("update exo_table set leftk=%s where id="+exo_id,(data[0]))
        self.cur_exo.execute("update exo_table set lefth=%s where id="+exo_id,(data[1]))
        self.cur_exo.execute("update exo_table set rightk=%s where id="+exo_id,(data[2]))
        self.cur_exo.execute("update exo_table set righth=%s where id="+exo_id,(data[3]))
        self.cur_exo.execute("update exo_table set temp=%s where id="+exo_id,(data[4]))
        self.cur_exo.execute("update exo_table set hum=%s where id="+exo_id,(data[5]))      
        self.cur_exo.execute("update exo_table set atmo=%s where id="+exo_id,(data[6]))  
        self.cur_exo.execute("update exo_table set longitude=%s where id="+exo_id,(data[7]))
        self.cur_exo.execute("update exo_table set latitude=%s where id="+exo_id,(data[8]))
        self.conn_exo.commit()
#将关节角度和环境数据的历史数据存放到先对应的数据库    
    def exo_log(self,data):
        time_stamp = time.asctime( time.localtime(time.time()) )
        time_tuple=(time_stamp,)
        log_data=time_tuple+data
        self.cur_exolog.execute("insert into exo_"+exo_id+" values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",log_data)
        self.conn_exolog.commit()
        
if __name__=="__main__":  
    rospy.init_node('data_subscriber',anonymous = True)
    exo_id = str(sys.argv[1])
    data_interface=Data_Interface()  
    rospy.spin()
