# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:58:43 2020

@author: Grupo
"""

import mysql.connector

def getConnection():
    connect = mysql.connector.connect(host= '127.0.0.1', 
                                         user = 'root', 
                                         password = '', 
                                         db = 'partialcourseadmission', 
                                         charset = 'utf8')
    return connect
