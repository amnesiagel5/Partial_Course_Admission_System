# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:31:02 2020

@author: Grupo #BSIT-2B
"""

import sys
from PyQt5 import  QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from MainGUI import Ui_MainWindow
from MainModel import mainWindowModel
from freshmenGUIController import freshmenWindowController
from transfereesGUIController import transfereesWindowController
from oldStudentsGUIController import oldStudentsWindowController
from secDegreeApplicantsGUIController import secondDegreeWindowController
from gradSchoolApplicantsGUIController import gradSchoolWindowController
from userGuide import Ui_formGuide
from about import Ui_formAbout
#import pandas as pd
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission' # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.

class mainWindowController(QMainWindow,Ui_MainWindow):  
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.btnIncomingFreshman.clicked.connect(self.openIncomingFreshmanWindow)
        self.btnOldStudent.clicked.connect(self.openOldStudentWindow)
        self.btnTransferee.clicked.connect(self.openTransfereeWindow)
        self.btnSecDegree.clicked.connect(self.openSecondDegreeWindow)
        self.btnGradSchool.clicked.connect(self.openGradSchoolWindow)
        self.btnUserGuide.clicked.connect(self.openUserGuideWindow)
        self.btnAbout.clicked.connect(self.openAboutWindow)
        self.btnImage.setIcon(QtGui.QIcon('image/pcas.png'))
        self.btnImage.setIconSize(QtCore.QSize(200,200))
        #self.holder = mainWindowModel()
        #self.holder.openUserGuideWindow()
        
    def openIncomingFreshmanWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = freshmenWindowController()
        self.ui.setupUi(self.window)
        self.all = freshmenWindowController()
        self.all.show()
        
    def openOldStudentWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = oldStudentsWindowController()
        self.ui.setupUi(self.window)
        self.all = oldStudentsWindowController()
        self.all.show()
    
    def openTransfereeWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = transfereesWindowController()
        self.ui.setupUi(self.window)
        self.all = transfereesWindowController()
        self.all.show() 
    
    def openGradSchoolWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = gradSchoolWindowController()
        self.ui.setupUi(self.window)
        self.all = gradSchoolWindowController()
        self.all.show()
        
    def openSecondDegreeWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = secondDegreeWindowController()
        self.ui.setupUi(self.window)
        self.all = secondDegreeWindowController()
        self.all.show()
        
    def openUserGuideWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_formGuide()
        self.ui.setupUi(self.window)
        self.all = Ui_formGuide()
        self.window.show()
        
    def openAboutWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_formAbout()
        self.ui.setupUi(self.window)
        self.all = Ui_formAbout()
        self.window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindowController()
    window.show()
    sys.exit(app.exec_())
