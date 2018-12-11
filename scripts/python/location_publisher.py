#!/usr/bin/env python
import rospy
from neu_wgg.msg import location
locat={"longitude":(123.4264419999999944),"latitude":(41.7721390000000028)}
def talker():
    location_pub = rospy.Publisher('location_topic', location, queue_size=10)
    rospy.init_node('location_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    longitude=0
    latitude=0
    i=0
    while not rospy.is_shutdown():
     longitude=locat["longitude"]
     latitude=locat["latitude"]
     location_msg= location()
     location_msg.longitude = longitude
     location_msg.latitude = latitude
     location_pub.publish(location_msg)
     i=i+1
     if i>3:
         i=0
     rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
