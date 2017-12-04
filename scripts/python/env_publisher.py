#!/usr/bin/env python
import rospy
from neu_wgg.msg import env

def talker():
    pub = rospy.Publisher('env_topic', env, queue_size=10)
    rospy.init_node('env_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        value = env()
	value.atmo = 1.5
	value.temp = 25.6
	value.hum = 31
        
        pub.publish(value)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
