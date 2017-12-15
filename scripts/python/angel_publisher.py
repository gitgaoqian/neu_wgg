#!/usr/bin/env python
# -*- coding: utf-8 -*-
#分别以sin cos来表示发布的4个关节角度值
import rospy
from neu_wgg.msg import angle
import math
def talker():
    i=0
    angle_pub = rospy.Publisher('angle_topic', angle, queue_size=10)
    rospy.init_node('angle_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        angle_msg=angle()
        data=math.sin(i)
        angle_msg.leftk=data
        angle_msg.lefth=data+1
        angle_msg.rightk=data+2
        angle_msg.righth=data+3
        angle_pub.publish(angle_msg)
        i = i+0.1
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass