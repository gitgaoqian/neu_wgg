#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import os
import sys
import thread
# Add custom service here
app = flask.Flask(__name__)

if "CLOUD_IP" not in os.environ:
    print "Can't find environment variable CLOUD_IP."
    sys.exit(1)

cloud_ip = os.environ['CLOUD_IP']
def data_storage(exo_number):
     os.system('python data_interface.py '+str(exo_number))
def data_fetch(exo_number):
     os.system('python monitor_interface.py '+str(exo_number))

@app.route('/cloud_service/<action>/<exo_number>', methods=['POST'])
def storage_and_fetch(action,exo_number):
    ros_master_ip = flask.request.remote_addr
    ros_master_uri = 'http://'+ros_master_ip+':11311'
    os.environ['ROS_MASTER_URI']=ros_master_uri
    os.environ['ROS_IP']=cloud_ip
    if action == "storage":
        thread.start_new_thread(data_storage,(exo_number,))
        return "cloud start store data to exo_table"
    elif action == "fetch":
        thread.start_new_thread(data_fetch,(exo_number,))
        return "cloud start fetch data from exo_table"  
    else:
        return action+" not permitted for exo_table! for monitor,set action=fetch;for exo,set action=storage"
        
if __name__ == '__main__':
    app.run(cloud_ip, 5566,threaded=True)
