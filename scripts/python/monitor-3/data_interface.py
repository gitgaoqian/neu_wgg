# -*- coding: utf-8 -*-
import MySQLdb as mdb
import rospy
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
exo_id=0

#将关节角度和环境数据存放到数据库
def callback(data):
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
     cur.execute("update exo_table set leftk=%s where id="+exo_id,(leftk))
     cur.execute("update exo_table set lefth=%s where id="+exo_id,(lefth))
     cur.execute("update exo_table set rightk=%s where id="+exo_id,(rightk))
     cur.execute("update exo_table set righth=%s where id="+exo_id,(righth))
     cur.execute("update exo_table set atmo=%s where id="+exo_id,(atmo))       
     cur.execute("update exo_table set hum=%s where id="+exo_id,(hum))      
     cur.execute("update exo_table set temp=%s where id="+exo_id,(temp))
     conn.commit()
if __name__=="__main__":  
    import sys  
    exo_id = str(sys.argv[1])
    rospy.init_node('data_subscriber',anonymous = True)
    conn=mdb.connect(host="127.0.0.1",user="root",db="exo1213",passwd="ubuntu",charset="utf8")
    cur=conn.cursor() 
    rospy.Subscriber('env_and_angle',env_and_angle,callback) 
    rospy.spin()
