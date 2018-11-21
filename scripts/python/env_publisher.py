#!/usr/bin/env python
import rospy
from neu_wgg.msg import env
def talker():
    env_pub = rospy.Publisher('env_topic', env, queue_size=10)
    rospy.init_node('env_pub', anonymous=True)
    rate = rospy.Rate(5) # 10hz
    atmo=1.0
    temp=15
    hum=60
    
    while not rospy.is_shutdown():
     atmo=atmo
     temp=temp
     hum=hum
     env_msg= env()
     env_msg.atmo = atmo
     env_msg.temp = temp
     env_msg.hum = hum
     env_pub.publish(env_msg)
     rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
