# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:15:12 2020

@author: Jelly Ann Pananganan #BSIT-2B
"""

import sys
import os  #,re
import connectionUtility
from connectionUtility import getConnection 
from PyQt5 import QtWidgets, QtCore ,QtGui
from PyQt5.QtWidgets import QApplication,QMessageBox
#from PyQt5.QtGui import QPixmap
from gradSchoolApplicantsGUI import Ui_GraduateSchool
from gradSchoolApplicantModel import gradSchoolModel
import pandas as pd
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission' # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.
con = getConnection()

class gradSchoolWindowController(QtWidgets.QWidget,Ui_GraduateSchool):
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
        self.btnImage.setIcon(QtGui.QIcon('image/gradschool.jpg'))
        self.btnImage.setIconSize(QtCore.QSize(200,200))
        
    def ClickAddButton(self):
        self.appendDataFromTextbox()
        self.holder = gradSchoolModel()
        self.holder.insertStudentData()
        if self.checkBoxTOR.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxGoodM.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxEnve.isChecked():
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease proceed at the Registrar Office & to your desired Course Department to fully enroll. Thank you!")
        else:
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease complete your requirements first to proceed at the Registrar Office & to your desired Course Department. Thank you!")
        
        
        self.ClearData()
        return
    
    def ClearData(self):
        self.txtID.setText('')
        self.txtLName.setText('')
        self.txtFName.setText('')
        self.txtMI.setText('')
        self.cmbCourse.setCurrentText('Select Desired Course')
        self.checkBoxTOR.setChecked(False)
        self.checkBoxNSO.setChecked(False)
        self.checkBoxGoodM.setChecked(False)
        self.checkBox2x2.setChecked(False)
        self.checkBoxEnve.setChecked(False)
        self.tableGradSchool.clearContents() 
        self.tableGradSchool.model().removeRows(0, self.tableGradSchool.rowCount())
        self.tableGradSchool.setRowCount(0)  
        self.tableGradSchool.reset()
        return
    
    def clickClearAll(self):
        self.cmbCourse.setCurrentText('Select Desired Course')
        return
    
    '''@QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.tableGradSchool.indexAt(button.pos()).row()
            self.tableGradSchool.removeRow(row)
        return'''
    
    def appendDataFromTextbox(self):
        self.IDNumber, self.LastName, self.FirstName, self.MI, self.DesiredCourse = self.getData()
        self.btnSubmit.clicked.connect(self.ClickSubmitButton)
        #numRows = self.tableGradSchool.rowCount()
        labels = ['IDNumber','LastName','FirstName','MI','Remarks','DesiredCourse'] 
        
        qtable_df = self.write_qtable_to_df(self.tableGradSchool) 
        #datalist = [] #empty list
        for idx, row in qtable_df.iterrows(): 
            mylist = [row.IDNumber, row.LastName, row.FirstName, row.MI, row.Remarks]
                
            l = mylist+[self.DesiredCourse]
            self.lista.append(l)
        
        zippedlist = list(self.lista)
        print(zippedlist)
        df = pd.DataFrame(zippedlist, columns = labels)  
       # insert the CSV file
        df.to_csv(os.path.join(path,r'gradSchoolApplicantsInfo.csv'), index = False)
        return df
    
    def ClickSubmitButton(self):
        self.IDNumber, self.LastName, self.FirstName, self.MI, self.DesiredCourse = self.getData()
        print(self.IDNumber, self.LastName, self.FirstName, self.MI, self.DesiredCourse, self.Remarks)
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
        IDNumber = self.txtID.text()
        LastName = self.txtLName.text()
        FirstName = self.txtFName.text()
        MI = self.txtMI.text()
        DesiredCourse = self.cmbCourse.currentText()
        
        if self.checkBoxTOR.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxGoodM.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxEnve.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        return IDNumber, LastName, FirstName, MI, DesiredCourse
    
    
    def addRow(self):
        self.IDNumber, self.LastName, self.FirstName, self.MI, self.DesiredCourse = self.getData()
        # Creates an empty row at bottom of table
        numRows = self.tableGradSchool.rowCount()
         
        self.tableGradSchool.insertRow(numRows)
        # Adds info/text to the row
        self.tableGradSchool.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.IDNumber))
        self.tableGradSchool.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.LastName))
        self.tableGradSchool.setItem(numRows, 2, QtWidgets.QTableWidgetItem(self.FirstName))
        self.tableGradSchool.setItem(numRows, 3, QtWidgets.QTableWidgetItem(self.MI))
        self.tableGradSchool.setItem(numRows, 4, QtWidgets.QTableWidgetItem(self.DesiredCourse))
        self.tableGradSchool.setItem(numRows, 5, QtWidgets.QTableWidgetItem(self.Remarks))
      
        self.tableGradSchool.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableGradSchool.resizeRowsToContents()
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
        selectQuery = "SELECT * FROM tbl_gradschool"
        cur = con.cursor()
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
        
        for row in record:
            if search ==  str(row[1]):
                self.ID = row[1]
                self.txtID.setText(str(self.ID))
                self.txtLName.setText(row[2])
                self.txtFName.setText(row[3])
                self.txtMI.setText(row[4])
                self.cmb = row[5]
                self.cmbCourse.setCurrentText(str(self.cmb))
                if row[6]=="Requirements are complete.\nQualified to enroll!":
                    self.checkBoxTOR.setChecked(True) 
                    self.checkBoxNSO.setChecked(True)
                    self.checkBoxGoodM.setChecked(True)
                    self.checkBox2x2.setChecked(True)
                    self.checkBoxEnve.setChecked(True)
                    QMessageBox.information(self, "NOTICE","Your requirements are already complete.")
                else:
                    self.checkBoxTOR.setChecked(False)
                    self.checkBoxNSO.setChecked(False)
                    self.checkBoxGoodM.setChecked(False)
                    self.checkBox2x2.setChecked(False)
                    self.checkBoxEnve.setChecked(False)
                    QMessageBox.information(self, "NOTICE","Your requirements are incomplete. Please comply first.")
                break
            
        else:
            QMessageBox.information(self,"NOTICE","Search doesn't match any ID Number!")    
        
        con.commit()
        cur.close()
        #return record
    
    def DataDelete(self):
        cur = con.cursor()
        selectQuery = "SELECT * FROM tbl_gradschool"
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
         
        for row in record:
            if search ==  str(row[1]):
                buttonReply = QMessageBox.question(self, 'DELETE RECORD', "Are you sure to delete your record?", QMessageBox.Yes , QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql_Delete_query = """Delete from tbl_gradschool where IDNumber = %s"""
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
        r3 = self.txtMI.text()
        r4 = self.cmbCourse.currentText()
        if self.checkBoxTOR.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxGoodM.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxEnve.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        selectQuery = "Update tbl_gradschool SET LastName = %s, FirstName = %s, MI = %s, DesiredCourse = %s, Remarks = %s WHERE IDNumber = %s" 
        search = str(self.txtSearch.text())
        equivalent = (r1, r2, r3, r4, self.Remarks, search)
        cur = con.cursor()
        cur.execute(selectQuery, equivalent)
        
        if self.checkBoxTOR.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxGoodM.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxEnve.isChecked():
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
    window = gradSchoolWindowController()
    window.show()
    sys.exit(app.exec_())
