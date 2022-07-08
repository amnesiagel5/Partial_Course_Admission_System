# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:31:46 2020

@author: Grupo
"""

#import connectionUtility
import pandas as pd
host = '127.0.0.1'
user = 'root'
password = ''
db = 'partialadmission'
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission'


class mainWindowModel():
    def __init__(self, parent = None):
        #self.cnx = connectionUtility.getConnection()
        super(self).__init__(parent)

        #the mainWindow does not need model file
        #'cause it does not communicate or use database connection
    
    '''def openOldStudentWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Old()
        self.ui.setupUi(self.window)
        self.all = Old()
        #self.window.show()
        self.all.show()
        
    def openIncomingFreshmanWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Freshmen()
        self.ui.setupUi(self.window)
        self.all = Freshmen()
        #self.window.show()
        self.all.show()
        
    def openTransfereeWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Transferee()
        self.ui.setupUi(self.window)
        self.all = Transferee()
        #self.window.show()
        self.all.show() 
    
    def openGradSchoolWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Grad()
        self.ui.setupUi(self.window)
        self.all = Grad()
        #self.window.show()
        self.all.show()
        
    def openSecondDegreeWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = secondDegreeWindowController()
        self.ui.setupUi(self.window)
        self.all = secondDegreeWindowController()
        self.window.show()
        #self.all.show()
        
    def openUserGuideWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_formGuide()
        self.ui.setupUi(self.window)
        self.all = Ui_formGuide()
        self.window.show()'''
        #self.all.show()   
   
if __name__ == "__main__":
    a = mainWindowModel()
    #a = openUserGuideWindow()
    
