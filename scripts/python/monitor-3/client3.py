#!/usr/bin/env python
import sys
import rospy
from neu_wgg.srv import call3

def local_client(id,act):

    rospy.wait_for_service('bridge_service')
    try:
        client = rospy.ServiceProxy('bridge_service', call3)
        resp = client(id,act)
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e
if __name__ == "__main__":
    rospy.init_node("client")
    # exo_id = str(rospy.get_param(param_name="~robotID",default="3"))
    # action = rospy.get_param(param_name="~action",default="store")
    exo_id = str(sys.argv[1])
    action = str(sys.argv[2])
    print " %s" %(local_client(exo_id,action))
