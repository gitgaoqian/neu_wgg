#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        time.sleep(2)
        #使用线程进行历史数据存储,这样设置可以使两个存储的频率不同
        thread.start_new_thread(self.exo_log,())
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
        self.update_exo()
#将关节角度和环境数据以及地理位置信息存放到数据库
    def update_exo(self):
        self.cur_exo.execute("update exo_table set leftk=%s where id="+exo_id,(self.leftk))
        self.cur_exo.execute("update exo_table set lefth=%s where id="+exo_id,(self.lefth))
        self.cur_exo.execute("update exo_table set rightk=%s where id="+exo_id,(self.rightk))
        self.cur_exo.execute("update exo_table set righth=%s where id="+exo_id,(self.righth))
        self.cur_exo.execute("update exo_table set temp=%s where id="+exo_id,(self.temp))
        self.cur_exo.execute("update exo_table set hum=%s where id="+exo_id,(self.hum))      
        self.cur_exo.execute("update exo_table set atmo=%s where id="+exo_id,(self.atmo))   
        self.cur_exo.execute("update exo_table set longitude=%s where id="+exo_id,(self.longitude))
        self.cur_exo.execute("update exo_table set latitude=%s where id="+exo_id,(self.latitude)) 
        self.conn_exo.commit()
#将关节角度和环境数据的历史数据存放到先对应的数据库    
    def exo_log(self):
        while 1:
#            time_stamp = time.asctime( time.localtime(time.time()) )
#            time_tuple=(time_stamp,)
            global num
            num=num+1
            num_tuple=(num,)
            data=(self.leftk,self.lefth,self.rightk,self.righth,self.temp,self.hum,self.atmo,self.longitude,self.latitude)
            log_data=num_tuple+data
            self.cur_exolog.execute("insert into exo_"+exo_id+" values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",log_data)
            time.sleep(2)
            self.conn_exolog.commit()
        
if __name__=="__main__":  
    rospy.init_node('data_subscriber',anonymous = True)
    exo_id = str(sys.argv[1])
    data_interface=Data_Interface()  
    rospy.spin()
