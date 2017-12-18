# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waiguge.ui'
#
# Created: Mon Nov 27 17:20:54 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import rospy
import os
import thread
from neu_wgg.msg import env_and_angle
#环境信息
atmo=0
temp=0
hum=0
#关节角度信息
leftk=0
lefth=0
rightk=0
righth=0
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
        Form.resize(590, 495)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 551, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.label_env1 = QtGui.QLabel(self.tab1)
        self.label_env1.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.label_env1.setObjectName(_fromUtf8("label_env1"))
        self.label_atmo1 = QtGui.QLabel(self.tab1)
        self.label_atmo1.setGeometry(QtCore.QRect(20, 70, 59, 30))
        self.label_atmo1.setObjectName(_fromUtf8("label_atmo1"))
        self.label_temp1 = QtGui.QLabel(self.tab1)
        self.label_temp1.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.label_temp1.setObjectName(_fromUtf8("label_temp1"))
        self.label_hum1 = QtGui.QLabel(self.tab1)
        self.label_hum1.setGeometry(QtCore.QRect(20, 150, 59, 15))
        self.label_hum1.setObjectName(_fromUtf8("label_hum1"))
        self.lineEdit_atmo1 = QtGui.QLineEdit(self.tab1)
        self.lineEdit_atmo1.setGeometry(QtCore.QRect(80, 75, 113, 23))
        self.lineEdit_atmo1.setObjectName(_fromUtf8("lineEdit_atmo1"))
        self.lineEdit_temp1 = QtGui.QLineEdit(self.tab1)
        self.lineEdit_temp1.setGeometry(QtCore.QRect(80, 108, 113, 23))
        self.lineEdit_temp1.setObjectName(_fromUtf8("lineEdit_temper1"))
        self.lineEdit_hum1 = QtGui.QLineEdit(self.tab1)
        self.lineEdit_hum1.setGeometry(QtCore.QRect(80, 145, 113, 23))
        self.lineEdit_hum1.setObjectName(_fromUtf8("lineEdit_hum1"))
        self.label_drv1 = QtGui.QLabel(self.tab1)
        self.label_drv1.setGeometry(QtCore.QRect(260, 20, 81, 31))
        self.label_drv1.setObjectName(_fromUtf8("label_drv1"))
        self.Button_leftk1 = QtGui.QPushButton(self.tab1)
        self.Button_leftk1.setGeometry(QtCore.QRect(250, 65, 100, 30))
        self.Button_leftk1.setObjectName(_fromUtf8("Button_leftk1"))
        self.Button_lefth1 = QtGui.QPushButton(self.tab1)
        self.Button_lefth1.setGeometry(QtCore.QRect(250, 120, 100, 30))
        self.Button_lefth1.setObjectName(_fromUtf8("Button_lefth1"))
        self.Button_rightk1 = QtGui.QPushButton(self.tab1)
        self.Button_rightk1.setGeometry(QtCore.QRect(390, 65, 100, 30))
        self.Button_rightk1.setObjectName(_fromUtf8("Button_rightk1"))
        self.Button_righth1 = QtGui.QPushButton(self.tab1)
        self.Button_righth1.setGeometry(QtCore.QRect(390, 120, 100, 30))
        self.Button_righth1.setObjectName(_fromUtf8("Button_righth1"))
#        self.Button_display1 = QtGui.QPushButton(self.tab1)
#        self.Button_display1.setGeometry(QtCore.QRect(50, 190, 80, 23))
#        self.Button_display1.setObjectName(_fromUtf8("Button_display1"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.header = QtGui.QLabel(Form)
        self.header.setGeometry(QtCore.QRect(230, 20, 151, 20))
        self.header.setObjectName(_fromUtf8("header"))
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_env1.setText(_translate("Form", "环境信息", None))
        self.label_atmo1.setText(_translate("Form", "大气压强", None))
        self.label_temp1.setText(_translate("Form", "温度", None))
        self.label_hum1.setText(_translate("Form", "湿度", None))
        self.label_drv1.setText(_translate("Form", "驱动信息", None))
        self.Button_leftk1.setText(_translate("Form", "左膝关节角度", None))
        self.Button_lefth1.setText(_translate("Form", "左髋关节角度", None))
        self.Button_rightk1.setText(_translate("Form", "右膝关节角度", None))
        self.Button_righth1.setText(_translate("Form", "右髋关节角度", None))
#        self.Button_display1.setText(_translate("Form", "显示", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "外骨骼"+str(exo_id), None))
        self.header.setText(_translate("Form", "外骨骼监控面板", None))

class mywindow(QtGui.QWidget,Ui_Form):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例   
        #订阅关节角度信息
        rospy.Subscriber('env_angle',env_and_angle,self.callback1)
       
        #槽函数链接
        self.Button_leftk1.clicked.connect(self.plot_leftk1)
        self.Button_lefth1.clicked.connect(self.plot_lefth1)
        self.Button_rightk1.clicked.connect(self.plot_rightk1)
        self.Button_righth1.clicked.connect(self.plot_righth1)
#        self.Button_display1.clicked.connect(self.env_display1)
    def callback1(self,data):
         global leftk
         global lefth
         global rightk
         global righth
         global atmo
         global temp
         global hum
         global exo_id
         atmo = data.atmo
         hum = data.hum
         temp = data.temp
         leftk=data.leftk
         lefth=data.lefth
         rightk=data.rightk
         righth=data.righth      
         self.lineEdit_atmo1.setText(str(atmo))
         self.lineEdit_temp1.setText(str(temp))
         self.lineEdit_hum1.setText(str(hum))
    def fun_leftk1(self):
        os.system('rosrun rqt_plot rqt_plot leftk')  
    def plot_leftk1(self):
        thread.start_new_thread(self.fun_leftk1,())
    def fun_lefth1(self):
        os.system('rosrun rqt_plot rqt_plot lefth')  
    def plot_lefth1(self):
        thread.start_new_thread(self.fun_lefth1,())
    def fun_rightk1(self):
        os.system('rosrun rqt_plot rqt_plot rightk')  
    def plot_rightk1(self):
        thread.start_new_thread(self.fun_rightk1,())
    def fun_righth1(self):
        os.system('rosrun rqt_plot rqt_plot rightk')  
    def plot_righth1(self):
        thread.start_new_thread(self.fun_righth1,())

if __name__=="__main__":  
    import sys  
    global exo_id
    exo_id = str(sys.argv[1])
    rospy.init_node('cloud_monitor',anonymous = True)
    app=QtGui.QApplication(sys.argv)  
    myshow=mywindow()  
    myshow.show()  
    sys.exit(app.exec_()) 
    
 


