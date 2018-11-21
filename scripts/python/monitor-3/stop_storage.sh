#!/bin/bash
# -*- coding: utf-8 -*-
# if语句中：if和［之间需有空格；［和变量之间有空格;判断用＂＝＂（或者test命令），且＝号两边需有空格
if [ $2 = 'store' ] #杀死采集节点和存储节点
then
{
	rosnode kill /StoreService_$1
	rosnode kill /Exo_$1
	rosnode kill /angle_publisher_$1
	rosnode kill /env_publisher_$1
	rosnode kill /location_publisher_$1
}
elif [ $2 = 'fetch' ]
then
{
	rosnode kill /FetchService_$1
}

fi
