#!bin/bash
# -*- coding: utf-8 -*-
# if语句中：if和［之间需有空格；［和变量之间有空格;判断用＂＝＂（或者test命令），且＝号两边需有空格
if [ $1 = 'stereo_proc' ]
then
{
	rosnode kill /base_link_to_camera_link
	rosnode kill /camera/stereo_image_proc
	rosnode kill /camera_link_to_laser
	rosnode kill /odom_publisher
	rosnode kill /pointcloud_to_laserscan
	rosnode kill /rviz
	rosnode kill /slam_gmapping
}
elif [ $1 = 'addition' ]
then
{
	rosnode kill /add_two_ints_server
}
elif [ $1 = 'keyboard_control' ]
then
{
	rosnode kill /teleop_turtle
}
else
	echo 'service not exist '
fi
