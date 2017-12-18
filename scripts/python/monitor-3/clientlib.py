# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:52:21 2017

@author: ros
"""
import requests
# 云端节点的注册
def cloud_param_set(url, master_uri):
    value = {'ros_master_uri': master_uri}
    r = requests.post(url, data=value)
    return r.text

# 根据不同表示服务的url实现不同云端服务的请求
def cloud_service_request(url):
    r = requests.post(url)
    return r.text
