#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
def main():
    items = {"output": "json", "ak": "deORyDWtAUIuqAOYN7O6f7ikELN2tsD9","address":"沈阳市东北大学"}
    r = requests.get("http://api.map.baidu.com/geocoder/v2/?address=沈阳东北大学&output=json&ak=deORyDWtAUIuqAOYN7O6f7ikELN2tsD9")
    print r
if __name__ == '__main__':
    main()