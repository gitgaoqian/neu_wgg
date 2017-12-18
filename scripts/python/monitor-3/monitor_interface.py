#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import rospy
from neu_wgg.msg import env_and_angle
#将关节角度和环境数据存放到数据库
def talker():  
    import sys  
    exo_id = str(sys.argv[1])
    data_pub=rospy.Publisher('env_angle',env_and_angle,queue_size=10) 
    rospy.init_node('data_publisher',anonymous = True)
    rate = rospy.Rate(5) # 10hz
    while not rospy.is_shutdown():
        conn=mdb.connect(host="127.0.0.1",user="root",db="exo1213",passwd="ubuntu",charset="utf8")
        cur=conn.cursor(cursorclass=mdb.cursors.DictCursor)
        cur.execute("select * from exo_table where id="+exo_id)
        result=cur.fetchall()
        cur.scroll(0,"absolute")
        atmo=result[0]["atmo"]
        temp=result[0]["temp"]
        hum=result[0]["hum"]
        leftk=result[0]["leftk"]
        lefth=result[0]["lefth"]
        rightk=result[0]["rightk"]
        righth=result[0]["righth"]
        msg= env_and_angle()
        msg.atmo = atmo
        msg.temp = temp
        msg.hum = hum
        msg.leftk=leftk
        msg.lefth=lefth
        msg.rightk=rightk
        msg.righth=righth
        data_pub.publish(msg)
        rate.sleep()       
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass   
