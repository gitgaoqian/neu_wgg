#!/usr/bin/env python
import rospy
import os
import sys
from neu_wgg.srv import call3 
import clientlib as bridge_client

if "CLOUD_IP" not in os.environ:
    print "Can't find environment variable CLOUD_IP."
    sys.exit(1)

# cloud_ip = os.environ['CLOUD_IP']
# cloud_service_port = 'http://'+ cloud_ip + ':5566'

def handle(data):
    exo_id= data.number
    action=data.action    
    url = "http://"+cloud_service_port + '/storage/'+exo_id+'/'+action
    return bridge_client.cloud_service_request(url)

def bridge_server():
    rospy.init_node('storage_bridge')
    rospy.Service('bridge_service', call3, handle)
    print "bridge_server ready for client."
    rospy.spin()

if __name__ == "__main__":
    cloud_service_port = str(sys.argv[1])
    bridge_server()

