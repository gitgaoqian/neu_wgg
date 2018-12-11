#!/usr/bin/env python
# -*- coding: utf-8 -*-
#采用实际采集的数据data by sun
import rospy
from neu_wgg.msg import angle
import math
import numpy as np
leftk = []
lefth = []
rightk = []
righth = []
def load_data(fileName):
    inFile = open(fileName, 'r')
    x = np.arange(1,3000,1)
    for line in inFile:
        data = line.strip('\n').split('\t')
        lefth.append(float(data[0]))
        leftk.append(float(data[2]))
        righth.append(float(data[4]))
        rightk.append(float(data[6]))

def talker():
    i=0
    load_data('/home/ros/catkin_ws/src/neu_wgg/scripts/python/data_wgg.txt')
    angle_pub = rospy.Publisher('angle_topic', angle, queue_size=10)
    rospy.init_node('angle_publisher', anonymous=True)
    rate = rospy.Rate(5) # 10hz
    while not rospy.is_shutdown():
        angle_msg=angle()
        # data=math.sin(i)
        angle_msg.leftk=leftk[i]
        angle_msg.lefth=lefth[i]
        angle_msg.rightk=rightk[i]
        angle_msg.righth=righth[i]
        angle_pub.publish(angle_msg)
        i = i + 1
        if i == 3000:
            i = 0
        # i = i+0.1
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass