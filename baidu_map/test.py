#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib

def main():
#    param = {"ak": "deORyDWtAUIuqAOYN7O6f7ikELN2tsD9"}
    urllib.urlretrieve("http://api.map.baidu.com/staticimage/v2?ak=deORyDWtAUIuqAOYN7O6f7ikELN2tsD9&center=123.425678,41.772176&zoom=18&markers=123.425678,41.772176","/home/ros/test/mymap.png")
if __name__=="__main__":  
    main()

