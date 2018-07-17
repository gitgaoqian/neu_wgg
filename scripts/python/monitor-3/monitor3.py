#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exo1226.ui'
#
# Created: Tue Dec 26 21:11:31 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
#增加关节期望角度.2018-7-15
from PyQt4 import QtCore, QtGui
import rospy
import os
import thread
from neu_wgg.msg import env_and_angle
import sys
pre_path = "/home/ros/pycharm/MyFiles/NEU_GDMAP/"
sys.path.append(pre_path+'neu_program')#把其他文件夹的py路径添加过来
import urllib
import cv2
import sign
#环境信息
atmo=0
temp=0
hum=0
#关节角度信息
elefk=0
elefh=0
erightk=0
erighth=0
leftk=0
lefth=0
rightk=0
righth=0
#地理位置信息
longitude=0
latitude=0
global exo_id
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(561, 790)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 521, 721))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.label_env = QtGui.QLabel(self.tab1)
        self.label_env.setGeometry(QtCore.QRect(10, 20, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_env.setFont(font)
        self.label_env.setObjectName(_fromUtf8("label_env"))
        self.label_atmo = QtGui.QLabel(self.tab1)
        self.label_atmo.setGeometry(QtCore.QRect(20, 70, 41, 21))
        self.label_atmo.setObjectName(_fromUtf8("label_atmo"))
        self.label_temp = QtGui.QLabel(self.tab1)
        self.label_temp.setGeometry(QtCore.QRect(20, 110, 81, 21))
        self.label_temp.setObjectName(_fromUtf8("label_temp"))
        self.label_hum = QtGui.QLabel(self.tab1)
        self.label_hum.setGeometry(QtCore.QRect(20, 150, 31, 21))
        self.label_hum.setObjectName(_fromUtf8("label_hum"))
        self.lineEdit_atmo = QtGui.QLineEdit(self.tab1)
        self.lineEdit_atmo.setGeometry(QtCore.QRect(60, 70, 71, 23))
        self.lineEdit_atmo.setObjectName(_fromUtf8("lineEdit_atmo"))
        self.lineEdit_temp = QtGui.QLineEdit(self.tab1)
        self.lineEdit_temp.setGeometry(QtCore.QRect(60, 110, 71, 23))
        self.lineEdit_temp.setObjectName(_fromUtf8("lineEdit_temp"))
        self.lineEdit_hum = QtGui.QLineEdit(self.tab1)
        self.lineEdit_hum.setGeometry(QtCore.QRect(60, 150, 71, 23))
        self.lineEdit_hum.setObjectName(_fromUtf8("lineEdit_hum"))
        self.label_drv = QtGui.QLabel(self.tab1)
        self.label_drv.setGeometry(QtCore.QRect(260, 30, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_drv.setFont(font)
        self.label_drv.setObjectName(_fromUtf8("label_drv"))
        self.Button_leftk = QtGui.QPushButton(self.tab1)
        self.Button_leftk.setGeometry(QtCore.QRect(240, 70, 101, 41))
        self.Button_leftk.setObjectName(_fromUtf8("Button_leftk"))
        self.Button_lefth = QtGui.QPushButton(self.tab1)
        self.Button_lefth.setGeometry(QtCore.QRect(240, 120, 101, 41))
        self.Button_lefth.setObjectName(_fromUtf8("Button_lefth"))
        self.Button_rightk = QtGui.QPushButton(self.tab1)
        self.Button_rightk.setGeometry(QtCore.QRect(370, 70, 111, 41))
        self.Button_rightk.setObjectName(_fromUtf8("Button_rightk"))
        self.Button_righth = QtGui.QPushButton(self.tab1)
        self.Button_righth.setGeometry(QtCore.QRect(370, 120, 111, 41))
        self.Button_righth.setObjectName(_fromUtf8("Button_righth"))
        self.label = QtGui.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(0, 190, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_long = QtGui.QLabel(self.tab1)
        self.label_long.setGeometry(QtCore.QRect(50, 230, 41, 21))
        self.label_long.setObjectName(_fromUtf8("label_long"))
        self.label_lat = QtGui.QLabel(self.tab1)
        self.label_lat.setGeometry(QtCore.QRect(200, 232, 41, 21))
        self.label_lat.setObjectName(_fromUtf8("label_lat"))
        self.lineEdit_long = QtGui.QLineEdit(self.tab1)
        self.lineEdit_long.setGeometry(QtCore.QRect(90, 230, 100, 27))
        self.lineEdit_long.setObjectName(_fromUtf8("lineEdit_long"))
        self.lineEdit_lat = QtGui.QLineEdit(self.tab1)
        self.lineEdit_lat.setGeometry(QtCore.QRect(240, 230, 100, 27))
        self.lineEdit_lat.setObjectName(_fromUtf8("lineEdit_lat"))
        self.Button_map = QtGui.QPushButton(self.tab1)
        self.Button_map.setGeometry(QtCore.QRect(350, 228, 71, 31))
        self.Button_map.setObjectName(_fromUtf8("Button_map"))
        self.label_map = QtGui.QLabel(self.tab1)
        self.label_map.setGeometry(QtCore.QRect(60, 280, 400, 400))
        self.label_map.setText(_fromUtf8(""))
        self.label_map.setObjectName(_fromUtf8("label_map"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.header = QtGui.QLabel(Form)
        self.header.setGeometry(QtCore.QRect(200, 20, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setObjectName(_fromUtf8("header"))
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_env.setText(_translate("Form", "环境信息", None))
        self.label_atmo.setText(_translate("Form", "温度", None))
        self.label_temp.setText(_translate("Form", "湿度", None))
        self.label_hum.setText(_translate("Form", "气压", None))
        self.label_drv.setText(_translate("Form", "运动信息", None))
        self.Button_leftk.setText(_translate("Form", "左膝关节角度", None))
        self.Button_lefth.setText(_translate("Form", "左髋关节角度", None))
        self.Button_rightk.setText(_translate("Form", "右膝关节角度", None))
        self.Button_righth.setText(_translate("Form", "右髋关节角度", None))
        self.label.setText(_translate("Form", "地理位置信息", None))
        self.label_long.setText(_translate("Form", "经度", None))
        self.label_lat.setText(_translate("Form", "纬度", None))
        self.Button_map.setText(_translate("Form", "地图显示", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "外骨骼"+str(exo_id), None))
        self.header.setText(_translate("Form", "外骨骼监控面板", None))
class mywindow(QtGui.QWidget,Ui_Form):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例   
        global exo_id
        topic_name = "fetch_topic_"+exo_id
        #订阅关节角度信息
        rospy.Subscriber(topic_name,env_and_angle,self.callback)
       
        #槽函数链接
        self.Button_leftk.clicked.connect(self.plot_leftk)
        self.Button_lefth.clicked.connect(self.plot_lefth)
        self.Button_rightk.clicked.connect(self.plot_rightk)
        self.Button_righth.clicked.connect(self.plot_righth)
        self.Button_map.clicked.connect(self.map_display)
#        self.Button_display1.clicked.connect(self.env_display1)
    def callback(self,data):
         global leftk
         global lefth
         global rightk
         global righth
         global atmo
         global temp
         global hum
         global longitude
         global latitude
         global exo_id
         atmo = data.atmo
         hum = data.hum
         temp = data.temp
         leftk=data.leftk
         lefth=data.lefth
         rightk=data.rightk
         righth=data.righth
         longitude=data.longitude
         latitude=data.latitude
         self.lineEdit_atmo.setText(str(atmo))
         self.lineEdit_temp.setText(str(temp))
         self.lineEdit_hum.setText(str(hum))
         self.lineEdit_long.setText(str(longitude))
         self.lineEdit_lat.setText(str(latitude))
    def fun_leftk(self):
        os.system('rosrun rqt_plot rqt_plot /angle_topic/leftk')  
    def plot_leftk(self):
        thread.start_new_thread(self.fun_leftk,())
    def fun_lefth(self):
        os.system('rosrun rqt_plot rqt_plot /angle_topic/lefth')  
    def plot_lefth(self):
        thread.start_new_thread(self.fun_lefth,())
    def fun_rightk(self):
        os.system('rosrun rqt_plot rqt_plot /angle_topic/rightk')  
    def plot_rightk(self):
        thread.start_new_thread(self.fun_rightk,())
    def fun_righth(self):
        os.system('rosrun rqt_plot rqt_plot /angle_topic/rightk')  
    def plot_righth(self):
        thread.start_new_thread(self.fun_righth,())
    def map_display(self):
        global longitude
        global latitude
        #在线模式
        # url="http://api.map.baidu.com/staticimage/v2?ak=deORyDWtAUIuqAOYN7O6f7ikELN2tsD9&center="+str(longitude)+","+str(latitude)+"&zoom=18&markers="+str(longitude)+","+str(latitude)
        # urllib.urlretrieve(url,"/home/ubuntu/NeuExoMap/mymap.png")
        #离线模式
        gd_lng = longitude
        gd_lat = latitude
        (tileX, tileY) = sign.GeographyToTile(gd_lng, gd_lat)  # 获取瓦片坐标
        (pixelX_init, pixelY_init) = sign.GeographyToPixel(gd_lng, gd_lat)  # 获取像素坐标
        (numX, numY, tileX_init, tileY_init) = sign.TileJudge(tileX, tileY)  # 判断瓦片落在哪一个部分,返回这个部分的左上角的瓦片坐标
        (pixelX, pixelY) = (pixelX_init + (int(tileX) - tileX_init) * 256, pixelY_init + (int(tileY) - tileY_init) * 256)  # 计算在该部分瓦片的像素坐标
        img = cv2.imread(pre_path+"/neu_tiles/" + str(numX) + "_" + str(numY) + "/tile_png/L18/neu.png")
        cv2.circle(img, (int(round(pixelX)), int(round(pixelY))), 10, (0, 0, 255), -1)
        img = cv2.resize(img,(400,400),interpolation=cv2.INTER_LINEAR)
        cv2.imwrite("/home/ros/NeuExoMap/mymap.png", img)
        image = QtGui.QImage("/home/ros/NeuExoMap/mymap.png")          
        self.label_map.setPixmap(QtGui.QPixmap.fromImage(image))         
        self.label_map.adjustSize() 

if __name__=="__main__":  
	exo_id = str(sys.argv[1])
	node_name = "Monitor_"+exo_id
	rospy.init_node(node_name,anonymous = True)
	app=QtGui.QApplication(sys.argv)  
	myshow=mywindow()  
	myshow.show()  
	sys.exit(app.exec_())
 




