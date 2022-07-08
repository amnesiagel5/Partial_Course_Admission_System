# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:00:17 2020

@author: Leizel Mae Barrit #BSIT-2B
"""

import sys
import os  #,re
import connectionUtility
from connectionUtility import getConnection 
from PyQt5 import QtWidgets ,QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
#from PyQt5.QtGui import QPixmap
from oldStudentsGUI import Ui_OldStudent
from oldStudentModel import oldStudentsModel
import pandas as pd
#import datetime
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission' # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.
con = getConnection()

class oldStudentsWindowController(QtWidgets.QWidget,Ui_OldStudent):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        self.setupUi(self)
        self.lista = [] 
        self.cnx = connectionUtility.getConnection()   
        self.cursor = self.cnx.cursor()
        # self.ui.setupUi(self)
        self.btnSubmit.clicked.connect(self.ClickSubmitButton) #preview
        self.btnAdd.clicked.connect(self.ClickAddButton)
        self.btnSearch.clicked.connect(self.ClickSearchButton)
        self.btnDelete.clicked.connect(self.ClickDeleteButton)
        self.btnUpdate.clicked.connect(self.ClickUpdateButton)
        self.btnClear.clicked.connect(self.clickClearAll)
        self.btnClearSearch.clicked.connect(self.clickClearAll)
        self.btnSearch.setIcon(QtGui.QIcon('image/icons8_Search_30px_1.png'))
        self.btnSearch.setIconSize(QtCore.QSize(50,50))
        self.btnImage.setIcon(QtGui.QIcon('image/oldstudent.jpg'))
        self.btnImage.setIconSize(QtCore.QSize(230,200))
        
    def ClickAddButton(self):
        self.appendDataFromTextbox()
        self.holder = oldStudentsModel()
        self.holder.insertStudentData()
        if self.checkBox.isChecked():
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease proceed at the Registrar Office & to your desired Course Department to fully enroll. Thank you!")
        else:
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease complete your requirements first to proceed at the Registrar Office & to your desired Course Department. Thank you!")
        
        self.ClearData()
        #self.deleteClicked()
        return
    
    def ClearData(self):
        self.txtLName.setText('')
        self.txtFName.setText('')
        self.txtMI.setText('')
        self.txtID.setText('')
        self.cmbCourse.setCurrentText('Select Course')
        self.cmbYear.setCurrentText('Select Year')
        self.cmbProgram.setCurrentText('Day/Night')
        self.checkBox.setChecked(False)
        self.tableOldStudent.clearContents() 
        self.tableOldStudent.model().removeRows(0, self.tableOldStudent.rowCount())
        self.tableOldStudent.setRowCount(0)
        self.tableOldStudent.reset()
        return
    
    def clickClearAll(self):
        self.cmbCourse.setCurrentText('Select Course')
        self.cmbYear.setCurrentText('Select Year')
        self.cmbProgram.setCurrentText('Day/Night')
        return
    
    '''@QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.tableOldStudent.indexAt(button.pos()).row()
            self.tableOldStudent.removeRow(row)
        return'''
        
    def appendDataFromTextbox(self):
        self.LastName, self.FirstName, self.MI, self.IDNumber, self.Course, self.Program, self.Year = self.getData()
        self.btnSubmit.clicked.connect(self.ClickSubmitButton)
        #numRows = self.tableOldStudent.rowCount()
        labels = ['LastName','FirstName','MI','IDNumber','Course','Remarks','Program', 'Year'] 
        
        qtable_df = self.write_qtable_to_df(self.tableOldStudent) 
        #datalist = [] #empty list
        for idx, row in qtable_df.iterrows(): 
            mylist = [row.LastName, row.FirstName, row.MI, row.IDNumber, row.Course, row.Remarks]
                
            l = mylist+[self.Program, self.Year]
            self.lista.append(l)
        
        zippedlist = list(self.lista)
        print(zippedlist)
        df = pd.DataFrame(zippedlist, columns = labels )  
       # insert the CSV file
        df.to_csv(os.path.join(path,r'oldStudentsInfo.csv'), index = False )
        return df
    
    def ClickSubmitButton(self):
        self.LastName, self.FirstName, self.MI, self.IDNumber, self.Course, self.Program, self.Year = self.getData()
        print(self.LastName, self.FirstName, self.MI, self.IDNumber, self.Course, self.Program, self.Year, self.Remarks)
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
    
    def getData(self):
        #assigning the variable names of the Object Names from the GUI
        LastName = self.txtLName.text()
        FirstName = self.txtFName.text()
        MI = self.txtMI.text()
        IDNumber = self.txtID.text()
        Course = self.cmbCourse.currentText()
        Program = self.cmbProgram.currentText()
        Year = self.cmbYear.currentText()
        
        if self.checkBox.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        return LastName, FirstName, MI, IDNumber, Course, Program, Year
    
    
    def addRow(self):
        self.LastName, self.FirstName, self.MI, self.IDNumber, self.Course, self.Program, self.Year = self.getData()
        # Creates an empty row at bottom of table
        numRows = self.tableOldStudent.rowCount()
         
        self.tableOldStudent.insertRow(numRows)
        # Adds info/text to the row
        self.tableOldStudent.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.LastName))
        self.tableOldStudent.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.FirstName))
        self.tableOldStudent.setItem(numRows, 2, QtWidgets.QTableWidgetItem(self.MI))
        self.tableOldStudent.setItem(numRows, 3, QtWidgets.QTableWidgetItem(self.IDNumber))
        self.tableOldStudent.setItem(numRows, 4, QtWidgets.QTableWidgetItem(self.Course))
        self.tableOldStudent.setItem(numRows, 5, QtWidgets.QTableWidgetItem(self.Program))
        self.tableOldStudent.setItem(numRows, 6, QtWidgets.QTableWidgetItem(self.Year))
        self.tableOldStudent.setItem(numRows, 7, QtWidgets.QTableWidgetItem(self.Remarks))
      
        self.tableOldStudent.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableOldStudent.resizeRowsToContents()
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
        selectQuery = "SELECT * FROM tbl_oldstudents"
        cur = con.cursor()
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
        
        for row in record:
            if search ==  str(row[4]):
                self.txtLName.setText(row[1]) #self.LastName
                self.txtFName.setText(row[2])
                self.txtMI.setText(row[3])
                self.ID = row[4]
                self.txtID.setText(str(self.ID))
                self.cmb = row[5]
                self.cmbCourse.setCurrentText(str(self.cmb))
                self.pg = row[6]
                self.cmbProgram.setCurrentText(str(self.pg))
                self.yr = row[7]
                self.cmbYear.setCurrentText(str(self.yr))
                if row[8]=="Requirements are complete.\nQualified to enroll!":
                    self.checkBox.setChecked(True) 
                    QMessageBox.information(self, "NOTICE","Your requirements are already complete.")
                else:
                    self.checkBox.setChecked(False)
                    QMessageBox.information(self, "NOTICE","Your requirements are incomplete. Please comply first.")
                break
            
        else:
            QMessageBox.information(self,"NOTICE","Search doesn't match any ID Number!")    
        
        con.commit()
        cur.close()
        #return record
    
    def DataDelete(self):
        cur = con.cursor()
        selectQuery = "SELECT * FROM tbl_oldstudents"
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
         
        for row in record:
            if search ==  str(row[4]):
                buttonReply = QMessageBox.question(self, 'DELETE RECORD', "Are you sure to delete your record?", QMessageBox.Yes , QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql_Delete_query = """Delete from tbl_oldstudents where IDNumber = %s"""
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
        r1 = self.txtLName.text()
        r2 = self.txtFName.text()
        r4 = self.txtMI.text()
        r5 = self.cmbCourse.currentText()
        r6 = self.cmbProgram.currentText()
        r7 = self.cmbYear.currentText()
        if self.checkBox.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        selectQuery = "Update tbl_oldstudents SET LastName = %s, FirstName = %s, MI = %s, Course = %s,Program = %s,Year = %s, Remarks = %s WHERE IDNumber = %s" 
        search = str(self.txtSearch.text())
        equivalent = (r1, r2, r4, r5, r6, r7, self.Remarks, search)
        cur = con.cursor()
        cur.execute(selectQuery, equivalent)
        
        if self.checkBox.isChecked():
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
    window = oldStudentsWindowController()
    window.show()
    sys.exit(app.exec_())