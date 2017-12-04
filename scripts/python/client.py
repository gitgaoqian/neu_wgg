#!/usr/bin/env python
import sys
import rospy
from neu_wgg.srv import call


def local_client(num):
    rospy.wait_for_service('bridge_service')
    try:
        client = rospy.ServiceProxy('bridge_service', call)
        resp = client(num)
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


if __name__ == "__main__":
    rospy.init_node('client')
    number = str(sys.argv[1])
    # srv_list = local_client('list_service', 'list')
    print " %s" % (local_client(number))

