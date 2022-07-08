# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:43:04 2020

@author: James Kenneth Cañedo #BSIT-2B
"""

import sys
import os  #,re
import connectionUtility
from connectionUtility import getConnection 
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
#from PyQt5.QtGui import QPixmap
from freshmenGUI import Ui_Freshmen
from freshmanModel import freshmenModel
import pandas as pd
import datetime
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission' # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.
con = getConnection()

class freshmenWindowController(QtWidgets.QWidget,Ui_Freshmen):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        self.setupUi(self)
        self.lista = [] 
        self.cnx = connectionUtility.getConnection()   
        self.cursor = self.cnx.cursor()
        # self.ui.setupUi(self)
        self.btnSubmit.clicked.connect(self.ClickSubmitButton) # preview
        self.btnAdd.clicked.connect(self.ClickAddButton)
        self.btnSearch.clicked.connect(self.ClickSearchButton)
        self.btnDelete.clicked.connect(self.ClickDeleteButton)
        self.btnUpdate.clicked.connect(self.ClickUpdateButton)
        self.btnDate.clicked.connect(self.onClicked)
        self.btnClear.clicked.connect(self.clickClearAll)
        self.btnClearSearch.clicked.connect(self.clickClearAll)
        self.btnSearch.setIcon(QtGui.QIcon('image/icons8_Search_30px_1.png'))
        self.btnSearch.setIconSize(QtCore.QSize(50,50))
        self.btnImage.setIcon(QtGui.QIcon('image/freshman.jpg'))
        self.btnImage.setIconSize(QtCore.QSize(198,190))
        
    def ClickAddButton(self):
        self.appendDataFromTextbox()
        self.holder = freshmenModel()
        self.holder.insertStudentData()
        if self.checkBox.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked() and self.checkBox_6.isChecked() and self.checkBox_7.isChecked() and self.checkBox_8.isChecked() or self.checkBox_5.isChecked():
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease proceed at the Registrar Office & to your desired Course Department to fully enroll. Thank you!")
        else:
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease complete your requirements first to proceed at the Registrar Office & to your desired Course Department. Thank you!")
        
        self.ClearData()
        #self.deleteClicked()
        return
    
    def ClearData(self):
        self.txtFName.setText('')
        self.txtMI.setText('')
        self.txtLName.setText('')
        self.txtPrev.setText('')
        self.cmbDCourse.setCurrentText('Select Course')
        self.txtAve.setText('')
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.Date.setText('')
        self.Time.setText('')
        self.tableFreshman.clearContents() 
        self.tableFreshman.setRowCount(0)
        self.tableFreshman.model().removeRows(0, self.tableFreshman.rowCount())
        self.tableFreshman.reset()
        return
    
    def clickClearAll(self):
        self.cmbDCourse.setCurrentText('Select Course')
        return
    
    '''@QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.tableGradSchool.indexAt(button.pos()).row()
            self.tableGradSchool.removeRow(row)
        return'''
        
    def appendDataFromTextbox(self):
        self.firstname, self.mi, self.lastname, self.previousschool, self.generalaverage, self.desiredcourse, self.date_a, self.time_a = self.getData()
        self.btnSubmit.clicked.connect(self.ClickSubmitButton)
        #numRows = self.tableFreshman.rowCount()
        labels = ['firstname','mi','lastname','previousschool','generalaverage','desiredcourse','remarks','date','time'] 
        
        qtable_df = self.write_qtable_to_df(self.tableFreshman) 
        #datalist = [] #empty list
        for idx, row in qtable_df.iterrows(): 
            mylist = [row.FirstName, row.MI, row.LastName, row.PreviousSchool, row.GenAverage,row.DesiredCourse, row.Remarks]
                
            l = mylist+[self.date_a, self.time_a]
            self.lista.append(l)
        
        zippedlist = list(self.lista)
        print(zippedlist)
        df = pd.DataFrame(zippedlist, columns = labels )  
       # insert the CSV file
        df.to_csv(os.path.join(path,r'freshmenInfo.csv'), index = False )
        return df
    
    def ClickSubmitButton(self):
        self.firstname, self.mi, self.lastname, self.previousschool, self.generalaverage, self.desiredcourse, self.date_a, self.time_a = self.getData()
        print(self.firstname, self.mi, self.lastname, self.previousschool, self.generalaverage, self.desiredcourse, self.Remarks)
        self.addRow()
        QMessageBox.information(self, "SUBMITTED", 'You can view your record now.')
        return
    
    def ClickSearchButton(self):
        self.DataSearch()
        return
        
    def ClickDeleteButton(self):
        self.DataDelete()
        return
    
    def ClickUpdateButton(self): 
        self.appendDataFromTextbox()
        self.DataUpdate()
        return
    
    def onClicked(self):
        DateTime = datetime.datetime.now()
        self.Date.setText(' %s-%s-%s ' % (DateTime.month, DateTime.day, DateTime.year))
        self.Time.setText(' %s:%s:%s ' % (DateTime.hour, DateTime.minute, DateTime.second))
    
    def getData(self):
        #assigning the variable names of the Object Names from the GUI
        #for printing the data in csv file
        firstname = self.txtFName.text()
        mi = self.txtMI.text()
        lastname = self.txtLName.text()
        previousschool = self.txtPrev.text()
        generalaverage = self.txtAve.text()
        #genaver = float(generalaverage)
        desiredcourse = self.cmbDCourse.currentText()
        date_a = self.Date.text()
        time_a = self.Time.text()
        
        if self.checkBox.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked() and self.checkBox_6.isChecked() and self.checkBox_7.isChecked() and self.checkBox_8.isChecked() or self.checkBox_5.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        return firstname, mi, lastname, previousschool, generalaverage, desiredcourse, date_a, time_a
    
    
    def addRow(self):
        self.firstname, self.mi, self.lastname, self.previousschool, self.generalaverage, self.desiredcourse, self.date_a, self.time_a = self.getData()
        # Creates an empty row at bottom of table
        numRows = self.tableFreshman.rowCount()
         
        self.tableFreshman.insertRow(numRows)
        # Adds info/text to the row
        self.tableFreshman.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.firstname))
        self.tableFreshman.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.mi))
        self.tableFreshman.setItem(numRows, 2, QtWidgets.QTableWidgetItem(self.lastname))
        self.tableFreshman.setItem(numRows, 3, QtWidgets.QTableWidgetItem(self.previousschool))
        self.tableFreshman.setItem(numRows, 4, QtWidgets.QTableWidgetItem(self.generalaverage))
        self.tableFreshman.setItem(numRows, 5, QtWidgets.QTableWidgetItem(self.desiredcourse))
        self.tableFreshman.setItem(numRows, 6, QtWidgets.QTableWidgetItem(self.Remarks))
      
        self.tableFreshman.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableFreshman.resizeRowsToContents()
        return
        
    def write_qtable_to_df(self, table):
        col_count = table.columnCount()
        row_count = table.rowCount()
        headers = [str(table.horizontalHeaderItem(i).text()) for i in range(col_count)]

        # df indexing is slow, so use lists
        df_list = []
        for row in range(row_count):
            df_list2 = []
            for col in range(col_count):
                table_item = table.item(row,col)
                df_list2.append('' if table_item is None else str(table_item.text()))
            df_list.append(df_list2)

        df = pd.DataFrame(df_list, columns=headers)
        return df
    
    def DataSearch(self):
        self.btnAdd.setEnabled(False)
        selectQuery = "SELECT * FROM tbl_freshmen"
        cur = con.cursor()
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
        
        for row in record:
            if search ==  str(row[1]):
                self.txtFName.setText(row[1])
                self.txtMI.setText(row[2])
                self.txtLName.setText(row[3])
                self.txtPrev.setText(row[4])
                self.cmb = row[5]
                self.cmbDCourse.setCurrentText(str(self.cmb))
                self.ave = row[6]
                self.txtAve.setText(str(self.ave))
                self.Date.setText(row[7])
                self.Time.setText(row[8])
                if row[9]=="Requirements are complete.\nQualified to enroll!":
                    self.checkBox.setChecked(True) 
                    self.checkBox_2.setChecked(True)
                    self.checkBox_3.setChecked(True)
                    self.checkBox_4.setChecked(True)
                    self.checkBox_5.setChecked(True)
                    self.checkBox_6.setChecked(True)
                    self.checkBox_7.setChecked(True)
                    self.checkBox_8.setChecked(True)
                    QMessageBox.information(self, "NOTICE","Your requirements are already complete.")
                else:
                    self.checkBox.setChecked(False)
                    self.checkBox_2.setChecked(False)
                    self.checkBox_3.setChecked(False)
                    self.checkBox_4.setChecked(False)
                    self.checkBox_5.setChecked(False)
                    self.checkBox_6.setChecked(False)
                    self.checkBox_7.setChecked(False)
                    self.checkBox_8.setChecked(False)
                    QMessageBox.information(self, "NOTICE","Your requirements are incomplete. Please comply first.")
                break
            
        else:
            QMessageBox.information(self,"NOTICE","Search doesn't match any first name!")    
        
        con.commit()
        cur.close()
        #return record
    
    def DataDelete(self):
        #con = getConnection()
        cur = con.cursor()
        selectQuery = "SELECT * FROM tbl_freshmen"
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
         
        for row in record:
            if search ==  str(row[1]):
                buttonReply = QMessageBox.question(self, 'DELETE RECORD', "Are you sure to delete your record?", QMessageBox.Yes , QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql_Delete_query = """Delete from tbl_freshmen where firstname = %s"""
                    seek = self.txtSearch.text()
                    cur.execute(sql_Delete_query, (seek,))
                    con.commit()
                    QMessageBox.information(self,"DELETED RECORD","Your record had successfully deleted.")
                    
                    self.txtSearch.setText('')
                    self.ClearData()
                    self.clickClearAll()
                    break
                else:
                    return
        else:
            QMessageBox.information(self,"DELETE RECORD","No record to delete.")
            self.txtSearch.setText('')
            con.commit()
            cur.close()
        self.btnAdd.setEnabled(True)
        return
    
    
    def DataUpdate(self):
        con = getConnection()
        name1 = self.txtMI.text()
        name2 = self.txtLName.text()
        name3 = self.txtPrev.text()
        name4 = self.txtAve.text()
        course = self.cmbDCourse.currentText()
        d1 = self.Date.text()
        d2 = self.Time.text()
        if self.checkBox.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked() and self.checkBox_6.isChecked() and self.checkBox_7.isChecked() and self.checkBox_8.isChecked() or self.checkBox_5.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
        
        selectQuery = "Update tbl_freshmen SET mi = %s, lastname = %s, previousschool = %s, generalaverage = %s, desiredcourse = %s, date = %s, time = %s, remarks = %s WHERE firstname = %s" 
        search = str(self.txtSearch.text())
        equivalent = (name1, name2, name3, name4, course, d1, d2, self.Remarks, search)
        cur = con.cursor()
        cur.execute(selectQuery, equivalent)
        if self.checkBox.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked() and self.checkBox_6.isChecked() and self.checkBox_7.isChecked() and self.checkBox_8.isChecked() or self.checkBox_5.isChecked():
            QMessageBox.information(self, "RECORD UPDATED","You had successfully updated your record.\nPlease proceed at the Registrar Office & to your desired Course Department to fully enroll. Thank you!")
        else:
            QMessageBox.information(self, "RECORD UPDATED","You had successfully updated your record.\nPlease complete your requirements first to proceed at the Registrar Office & to your desired Course Department. Thank you!")
        
        self.ClearData()
        self.clickClearAll()
        self.txtSearch.setText('')
        con.commit()
        cur.close()
        return
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = freshmenWindowController()
    window.show()
    sys.exit(app.exec_())