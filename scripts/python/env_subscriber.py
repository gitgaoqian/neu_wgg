#!/usr/bin/env python
import rospy
from neu_wgg.msg import env
global atmo
global hum
global temp
def callback(data):
    atmo = data.atmo
    hum = data.hum
    temp = data.temp
    #print atmo
    #print hum
    #print temp
if __name__=="__main__":   
        rospy.init_node('env_pub',anonymous = True)
        rospy.Subscriber('env_topic',env,callback)
        rospy.spin()

