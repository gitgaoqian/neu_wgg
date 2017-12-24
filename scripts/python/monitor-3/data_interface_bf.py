#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import rospy
from neu_wgg.msg import env_and_angle
import sys  
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
class Data_Interface:
    def __init__(self):
        rospy.Subscriber('env_and_angle',env_and_angle,self.callback) 
        self.conn=mdb.connect(host="127.0.0.1",user="root",db="exo1213",passwd="ubuntu",charset="utf8")
        self.cur=self.conn.cursor() 
#将关节角度和环境数据存放到数据库
    def callback(self,data):
        global leftk
        global lefth
        global rightk
        global righth
        global atmo
        global temp
        global hum
        global exo_id
        atmo = data.atmo
        hum = data.hum
        temp = data.temp
        leftk=data.leftk
        lefth=data.lefth
        rightk=data.rightk
        righth=data.righth
        self.cur.execute("update exo_table set leftk=%s where id="+exo_id,(leftk))
        self.cur.execute("update exo_table set lefth=%s where id="+exo_id,(lefth))
        self.cur.execute("update exo_table set rightk=%s where id="+exo_id,(rightk))
        self.cur.execute("update exo_table set righth=%s where id="+exo_id,(righth))
        self.cur.execute("update exo_table set atmo=%s where id="+exo_id,(atmo))       
        self.cur.execute("update exo_table set hum=%s where id="+exo_id,(hum))      
        self.cur.execute("update exo_table set temp=%s where id="+exo_id,(temp))
        self.conn.commit()
if __name__=="__main__":  
    rospy.init_node('data_subscriber',anonymous = True)
    exo_id = str(sys.argv[1])
    data_interface=Data_Interface()  
    rospy.spin()
