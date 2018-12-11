#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import rospy
import sys
from neu_wgg.msg import env_and_angle
#将关节角度和环境数据存放到数据库
def Monitor():
    exo_id = sys.argv[1]
    node_name = "Fetch_" + exo_id
    topic_name = "fetch_topic_"+exo_id
    data_pub=rospy.Publisher(topic_name,env_and_angle,queue_size=10)
    rospy.init_node(node_name,anonymous = True)
    rate = rospy.Rate(5) # 10hz
    while not rospy.is_shutdown():
        conn=mdb.connect(host="127.0.0.1",user="root",db="NeuExo",passwd="ubuntu",charset="utf8")
        cur=conn.cursor(cursorclass=mdb.cursors.DictCursor)
        cur.execute("select * from exo_sum where id="+exo_id)
        result=cur.fetchall()
        cur.scroll(0,"absolute")
        atmo=result[0]["atmo"]
        temp=result[0]["temp"]
        hum=result[0]["hum"]
        leftk=result[0]["leftk"]
        lefth=result[0]["lefth"]
        rightk=result[0]["rightk"]
        righth=result[0]["righth"]
        longitude=result[0]["longitude"]
        latitude=result[0]["latitude"]
        msg= env_and_angle()
        msg.atmo = atmo
        msg.temp = temp
        msg.hum = hum
        msg.leftk=leftk
        msg.lefth=lefth
        msg.rightk=rightk
        msg.righth=righth
        msg.longitude=longitude
        msg.latitude=latitude
        data_pub.publish(msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        Monitor()
    except rospy.ROSInterruptException:
        pass
