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


def Storage(exo_number):
    os.system('rosrun neu_wgg storage_interface.py ' + str(exo_number))


def Fetch(exo_number):
    os.system('rosrun neu_wgg monitor_interface.py ' + str(exo_number))


@app.route('/cloud_service/<exo_number>/<action>', methods=['POST'])
def ServiceHandler(exo_number, action):
    ros_master_ip = flask.request.remote_addr
    ros_master_uri = 'http://' + ros_master_ip + ':11311'
    os.environ['ROS_MASTER_URI'] = ros_master_uri
    os.environ['ROS_IP'] = cloud_ip
    if action == "storage":
        thread.start_new_thread(Storage, (exo_number,))
        return "store data to exo_table"
    elif action == "fetch":
        thread.start_new_thread(Fetch, (exo_number,))
        return "fetch data from exo_table"
    else:
        return action + " not permitted for exo_table! for Monitor,action=fetch;for EXO,action=storage"


if __name__ == '__main__':
    app.run(cloud_ip, 7788, threaded=True)
