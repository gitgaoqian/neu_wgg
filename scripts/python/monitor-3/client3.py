#!/usr/bin/env python
import sys
import rospy
from neu_wgg.srv import call3

def local_client(act,number):
    rospy.wait_for_service('bridge_service')
    try:
        client = rospy.ServiceProxy('bridge_service', call3)
        resp = client(act,number)
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == "__main__":
    action = str(sys.argv[1])
    exo_number = str(sys.argv[2])
    # srv_list = local_client('list_service', 'list')
    print " %s" %(local_client(action,exo_number))
