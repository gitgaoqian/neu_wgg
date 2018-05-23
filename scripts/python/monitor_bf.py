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
from smartcar.msg import env
from std_msgs.msg import Float64
#环境信息
global atmo
global temp
global hum
#关节角度信息
global leftk
global lefth
global rightk
global righth
global exo_id
import MySQLdb as mdb
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
        self.Button_display1 = QtGui.QPushButton(self.tab1)
        self.Button_display1.setGeometry(QtCore.QRect(50, 190, 80, 23))
        self.Button_display1.setObjectName(_fromUtf8("Button_display1"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
#        self.tab2 = QtGui.QWidget()
#        self.tab2.setObjectName(_fromUtf8("tab2"))
#        self.label_env2 = QtGui.QLabel(self.tab2)
#        self.label_env2.setGeometry(QtCore.QRect(20, 20, 81, 31))
#        self.label_env2.setObjectName(_fromUtf8("label_env2"))
#        self.label_atmo2 = QtGui.QLabel(self.tab2)
#        self.label_atmo2.setGeometry(QtCore.QRect(20, 70, 59, 30))
#        self.label_atmo2.setObjectName(_fromUtf8("label_atmo2"))
#        self.lineEdit_atmo2 = QtGui.QLineEdit(self.tab2)
#        self.lineEdit_atmo2.setGeometry(QtCore.QRect(80, 75, 113, 23))
#        self.lineEdit_atmo2.setObjectName(_fromUtf8("lineEdit_atmo2"))
#        self.label_temp2 = QtGui.QLabel(self.tab2)
#        self.label_temp2.setGeometry(QtCore.QRect(20, 110, 71, 16))
#        self.label_temp2.setObjectName(_fromUtf8("label_temp2"))
#        self.lineEdit_temp2 = QtGui.QLineEdit(self.tab2)
#        self.lineEdit_temp2.setGeometry(QtCore.QRect(80, 108, 113, 23))
#        self.lineEdit_temp2.setObjectName(_fromUtf8("lineEdit_temp2"))
#        self.label_hum2 = QtGui.QLabel(self.tab2)
#        self.label_hum2.setGeometry(QtCore.QRect(20, 150, 59, 15))
#        self.label_hum2.setObjectName(_fromUtf8("label_hum2"))
#        self.lineEdit_hum2 = QtGui.QLineEdit(self.tab2)
#        self.lineEdit_hum2.setGeometry(QtCore.QRect(80, 145, 113, 23))
#        self.lineEdit_hum2.setObjectName(_fromUtf8("lineEdit_hum2"))
#        self.label_drv2 = QtGui.QLabel(self.tab2)
#        self.label_drv2.setGeometry(QtCore.QRect(260, 20, 81, 31))
#        self.label_drv2.setObjectName(_fromUtf8("label_drv2"))
#        self.Button_leftk2 = QtGui.QPushButton(self.tab2)
#        self.Button_leftk2.setGeometry(QtCore.QRect(250, 65, 100, 30))
#        self.Button_leftk2.setObjectName(_fromUtf8("Button_leftk2"))
#        self.Button_lefth2 = QtGui.QPushButton(self.tab2)
#        self.Button_lefth2.setGeometry(QtCore.QRect(250, 120, 100, 30))
#        self.Button_lefth2.setObjectName(_fromUtf8("Button_lefth2"))
#        self.Button_rightk2 = QtGui.QPushButton(self.tab2)
#        self.Button_rightk2.setGeometry(QtCore.QRect(390, 65, 100, 30))
#        self.Button_rightk2.setObjectName(_fromUtf8("Button_rightk2"))
#        self.Button_righth2 = QtGui.QPushButton(self.tab2)
#        self.Button_righth2.setGeometry(QtCore.QRect(390, 120, 100, 30))
#        self.Button_righth2.setObjectName(_fromUtf8("Button_righth2"))
#        self.Button_display2 = QtGui.QPushButton(self.tab2)
#        self.Button_display2.setGeometry(QtCore.QRect(50, 190, 80, 23))
#        self.Button_display2.setObjectName(_fromUtf8("Button_display2"))
#        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
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
        self.Button_display1.setText(_translate("Form", "显示", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "外骨骼"+str(exo_id), None))
#        self.label_env2.setText(_translate("Form", "环境信息", None))
#        self.label_atmo2.setText(_translate("Form", "大气压强", None))
#        self.label_temp2.setText(_translate("Form", "温度", None))
#        self.label_hum2.setText(_translate("Form", "湿度", None))
#        self.label_drv2.setText(_translate("Form", "驱动信息", None))
#        self.Button_leftk2.setText(_translate("Form", "左膝关节角度", None))
#        self.Button_lefth2.setText(_translate("Form", "左髋关节角度", None))
#        self.Button_rightk2.setText(_translate("Form", "右膝关节角度", None))
#        self.Button_righth2.setText(_translate("Form", "右髋关节角度", None))
#        self.Button_display2.setText(_translate("Form", "显示", None))
#        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "外骨骼２", None))
        self.header.setText(_translate("Form", "外骨骼监控面板", None))

class mywindow(QtGui.QWidget,Ui_Form):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例   
        rospy.Subscriber('leftk',Float64,self.leftk_callback)
        rospy.Subscriber('lefth',Float64,self.lefth_callback)
        rospy.Subscriber('rightk',Float64,self.rightk_callback)
        rospy.Subscriber('righth',Float64,self.righth_callback)
        #槽函数链接
        self.Button_leftk1.clicked.connect(self.plot_leftk1)
        self.Button_lefth1.clicked.connect(self.plot_lefth1)
        self.Button_rightk1.clicked.connect(self.plot_rightk1)
        self.Button_righth1.clicked.connect(self.plot_righth1)
        
#        
#        self.Button_leftk2.clicked.connect(self.plot)
#        self.Button_lefth2.clicked.connect(self.plot)
#        self.Button_rightk2.clicked.connect(self.plot)
#        self.Button_righth2.clicked.connect(self.plot)
        
        self.Button_display1.clicked.connect(self.env_display1)
#        self.Button_display2.clicked.connect(self.env_display2)
    #将关节角度信息存放到数据库中
    def leftk_callback(self,data):
        global leftk
        global exo_id
        leftk=data.data
        cur.execute("update exo_table set atmo=%s where id="+exo_id,(leftk))
        conn.commit()
    def lefth_callback(self,data):
        global lefth
        global exo_id
        lefth=data.data
        cur.execute("update exo_table set atmo=%s where id="+exo_id,(lefth))
        conn.commit()
    def rightk_callback(self,data):
        global rightk
        global exo_id
        rightk=data.data
        cur.execute("update exo_table set atmo=%s where id="+exo_id,(rightk))
        conn.commit()
    def righth_callback(self,data):
        global righth
        global exo_id
        righth=data.data
        cur.execute("update exo_table set atmo=%s where id="+exo_id,(righth))
        conn.commit()
    #将环境信息存放在数据库并且在面板上显示
    def env_callback1(self,data):
        global atmo
        global temp
        global hum
        global exo_id
        atmo = data.atmo
        hum = data.hum
        temp = data.temp
        cur.execute("update exo_table set atmo=%s where id="+exo_id,(atmo))
        cur.execute("update exo_table set hum=%s where id="+exo_id,(hum))
        cur.execute("update exo_table set temp=%s where id="+exo_id,(temp))
        conn.commit()
        self.lineEdit_atmo1.setText(str(atmo))
        self.lineEdit_temp1.setText(str(temp))
        self.lineEdit_hum1.setText(str(hum))
        
#    def callback2(self,data):
#        global atmo
#        global temp
#        global hum
#        atmo = data.atmo
#        hum = data.hum
#        temp = data.temp
#        self.lineEdit_atmo2.setText(str(atmo))
#        self.lineEdit_temp2.setText(str(temp))
#        self.lineEdit_hum2.setText(str(hum))
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
    def env_display1(self):
        rospy.Subscriber('env_topic',env,self.env_callback1)
#    def env_display2(self):
#        rospy.Subscriber('env_monitor',env,self.callback2)

if __name__=="__main__":  
    import sys  
    global exo_id
    exo_id = str(sys.argv[1])
    rospy.init_node('cloud_monitor',anonymous = True)
    conn=mdb.connect(host="127.0.0.1",user="root",db="exo1213",passwd="ubuntu",charset="utf8")
    cur=conn.cursor()    
    app=QtGui.QApplication(sys.argv)  
    myshow=mywindow()  
    myshow.show()  
    sys.exit(app.exec_()) 
    
 


