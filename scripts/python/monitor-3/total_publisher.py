#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from neu_wgg.msg import sensor
from neu_wgg.msg import angle
from neu_wgg.msg import env_and_angle
# 环境信息
atmo = 0
temp = 0
hum = 0
# 关节角度信息
leftk = 0
lefth = 0
rightk = 0
righth = 0
exo_id = 0
# 地理位置信息
longitude = 0
latitude = 0


class data_publisher:
    def __init__(self):
        self.pub = rospy.Publisher('store_topic', env_and_angle, queue_size=10)
        rospy.Subscriber('sensor_topic', sensor, self.sensor_callback)
        rospy.Subscriber('angle_topic', angle, self.angle_callback)
        self.publish_data()

    def sensor_callback(self, data):
        global atmo
        global temp
        global hum
        global longitude
        global latitude
        longitude = data.longitude
        latitude = data.latitude
        atmo = data.atmo
        hum = data.hum
        temp = data.temp

    def angle_callback(self, data):
        global leftk
        global lefth
        global rightk
        global righth
        leftk = data.leftk
        lefth = data.lefth
        rightk = data.rightk
        righth = data.righth

    def publish_data(self):
        global atmo
        global temp
        global hum
        global leftk
        global lefth
        global rightk
        global righth
        global longitude
        global latitude
        rate = rospy.Rate(5)  # 10hz
        while not rospy.is_shutdown():
            msg = env_and_angle()
            msg.atmo = atmo
            msg.temp = temp
            msg.hum = hum
            msg.leftk = leftk
            msg.lefth = lefth
            msg.rightk = rightk
            msg.righth = righth
            msg.longitude = longitude
            msg.latitude = latitude
            self.pub.publish(msg)
            rate.sleep()


if __name__ == "__main__":
    rospy.init_node('data_publisher', anonymous=True)
    data_publisher()




