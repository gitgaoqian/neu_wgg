# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test/mymap.ui'
#
# Created: Tue Dec 26 15:08:39 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import urllib

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
        Form.resize(454, 402)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 71, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 30, 71, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 30, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 400, 300))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "经度", None))
        self.label_2.setText(_translate("Form", "纬度", None))
        self.pushButton.setText(_translate("Form", "显示地图", None))
        
class mywindow(QtGui.QWidget,Ui_Form):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例   
        #槽函数链接
        self.pushButton.clicked.connect(self.map_display)
    def map_display(self):
        url="http://api.map.baidu.com/staticimage/v2?ak=deORyDWtAUIuqAOYN7O6f7ikELN2tsD9&center=123.425678,41.772176&zoom=18&markers=123.425678,41.772176"
        urllib.urlretrieve(url,"/home/ros/test/mymap.png")        
        image = QtGui.QImage("/home/ros/test/mymap.png")          
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(image))         
        self.label_3.adjustSize() 


if __name__=="__main__":  
    import sys  
    app=QtGui.QApplication(sys.argv)  
    myshow=mywindow()  
    myshow.show() 
    sys.exit(app.exec_())  
