#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import os
import sys
import thread
import MySQLdb as mdb



def IsExoInExoSum(robotID):
    rows = cur.execute("select * from exo_sum where id=%s", (robotID))
    if rows == 0:
        return False
    else:
        return True
def InsertExoSum(robotID):
        cur.execute("insert into exo_sum values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (robotID,None,None,None,None,
                                                                                        None,None,None,None,None))
        conn.commit()
def CreateExoID(robotID):
        cur.execute("create table exo_"+str(robotID)+" (count int primary key,leftk float,lefth float,"
                                                         "rightk float,righth float,temp float,hum float,"
                                                         "atmo float,longitude float,latitude float)")
def Update():
        cur.execute("update exo_sum set leftk=%s,lefth=%s,rightk=%s,righth=%s,temp=%s,hum=%s,atmo=%s,longitude=%s,"
                    "latitude=%s where id=1",(3,4,5,6,7,8,9,2,1))
        conn.commit()
def Clear():
        cur.execute("truncate table exo_1")
        conn.commit()
if __name__ == '__main__':
    conn = mdb.connect(host="127.0.0.1", user="root", db="NeuExo", passwd="ubuntu", charset="utf8")
    cur = conn.cursor()
    a = Clear()
