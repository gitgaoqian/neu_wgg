# -*- coding: utf-8 -*-


import flask
import os
import sys
import thread

# Add custom service here
services_list = ['vision', 'stereo_proc']
app = flask.Flask(__name__)

if "CLOUD_IP" not in os.environ:
    print "Can't find environment variable CLOUD_IP."
    sys.exit(1)

cloud_ip = os.environ['CLOUD_IP']


def service_start(srv):
    if srv == 'vision':
        os.system('roslaunch drv_brain drv_v2_workstation.launch')
    # Add custom service here
    elif srv == 'stereo_proc':
        os.system('roslaunch mycamera stereo_proc.launch')
    else:
        return 'service not exist!'

@app.route('/cloud_service/<service>/<action>', methods=['POST'])
def cloud_service(service, action):
    ros_master_ip = flask.request.remote_addr
    ros_master_uri = 'http://'+ros_master_ip+':11311'
    os.environ['ROS_MASTER_URI']=ros_master_uri
    os.environ['ROS_IP']=cloud_ip
    if action == 'start':
        thread.start_new_thread(service_start, (service,))
        return "service " + service + " starting"
    elif action == 'stop':
        os.system('sh ~/cloud_test/stop.sh ' + service)
        return "service " + service + " closing"
    elif action == 'list':
        return str(services_list)
    elif action == 'start_all':
        for service in services_list:
            thread.start_new_thread(service_start, (service,))
        return "All services started."
    elif action == 'stop_all':
        for service in services_list:
            os.system('sh ~/cloud_test/stop.sh ' + service)
        return "All services stopped."
    else:
        return 'Action unknown, acceptable actions are:' \
               'start, stop, list, start_all, stop_all!'


if __name__ == '__main__':
    app.run(cloud_ip, 5566)
