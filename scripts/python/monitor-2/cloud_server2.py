#!/usr/bin/env python
# -*- coding: utf-8 -*-


import flask
import os
import sys
import thread
# Add custom service here
services_list = ['monitor','addition','stereo_proc']
app = flask.Flask(__name__)

if "CLOUD_IP" not in os.environ:
    print "Can't find environment variable CLOUD_IP."
    sys.exit(1)

cloud_ip = os.environ['CLOUD_IP']
def monitor(number):
     os.system('python monitor2.py '+str(number))

@app.route('/cloud_service/monitor/<number>', methods=['POST'])
def cloud_service(number):
    ros_master_ip = flask.request.remote_addr
    ros_master_uri = 'http://'+ros_master_ip+':11311'
    os.environ['ROS_MASTER_URI']=ros_master_uri
    os.environ['ROS_IP']=cloud_ip
    thread.start_new_thread(monitor,(number,))
   
    return "cloud start monitor service for exo"+'-'+str(number)
    
if __name__ == '__main__':
    app.run(cloud_ip, 5566,threaded=True)
