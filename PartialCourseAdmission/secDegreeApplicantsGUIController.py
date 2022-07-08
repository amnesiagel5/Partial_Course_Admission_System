# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:53:00 2020

@author: Mary Angel Fuentes #BSIT-2B
"""
import sys
import os  #re
import connectionUtility
from connectionUtility import getConnection 
from PyQt5 import QtWidgets ,QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
#from PyQt5.QtGui import QPixmap
from secDegreeApplicantsGUI import Ui_SecDegree
from secDegreeApplicantModel import secondDegreeModel
import pandas as pd
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission' # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.
from datetime import datetime
con = getConnection()

class secondDegreeWindowController(QtWidgets.QWidget,Ui_SecDegree):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        self.setupUi(self)
        self.lista = [] 
        self.cnx = connectionUtility.getConnection()   
        self.cursor = self.cnx.cursor()
        # self.ui.setupUi(self)
        # each button - create a function to perform tasks
        self.btnSubmit.clicked.connect(self.ClickSubmitButton) # previews all input from the user's information to the GUI
        self.btnAdd.clicked.connect(self.ClickAddButton)
        self.btnSearch.clicked.connect(self.ClickSearchButton)
        self.btnUpdate.clicked.connect(self.ClickUpdateButton)
        self.btnDelete.clicked.connect(self.ClickDeleteButton)
        self.btnClear.clicked.connect(self.clickClearAll)
        self.btnClearSearch.clicked.connect(self.clickClearAll)
        self.btnSearch.setIcon(QtGui.QIcon('image/icons8_Search_30px_1.png'))
        self.btnSearch.setIconSize(QtCore.QSize(50,50))
        self.btnImage.setIcon(QtGui.QIcon('image/secdegree.jpg'))
        self.btnImage.setIconSize(QtCore.QSize(200,200))
        
    def ClickAddButton(self):
        self.appendDataFromTextbox()
        self.holder = secondDegreeModel()
        self.holder.insertStudentData()
        if self.chkboxTOR.isChecked() and self.chkboxGoodMoral.isChecked() and self.chkbox12X2.isChecked() and self.chkboxTF400.isChecked() or self.chkboxTF300.isChecked():
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease proceed at the Registrar Office to fully enroll. Thank you!")
        else:
            QMessageBox.information(self, "RECORD ADDED","You had successfully added your record.\nPlease complete your requirements first to proceed at the Registrar Office. Thank you!")
        
        self.ClearData()
        #self.deleteClicked()
        return
    
    def ClearData(self):
        self.txtFName.setText('')
        self.txtMI.setText('')
        self.txtLName.setText('')
        self.cmbCourses.setCurrentText('Available Courses')
        self.chkboxTOR.setChecked(False)
        self.chkboxGoodMoral.setChecked(False)
        self.chkbox12X2.setChecked(False)
        self.chkboxTF400.setChecked(False)
        self.chkboxTF300.setChecked(False)
        self.tableSecDegree.reset()
        self.tableSecDegree.clearContents() 
        self.tableSecDegree.model().removeRows(0, self.tableSecDegree.rowCount())
        self.tableSecDegree.setRowCount(0)
        return
    
    def clickClearAll(self):
        self.cmbCourses.setCurrentText('Available Courses')
        self.DateAdmission.setDate(QtCore.QDate(2020, 5, 1))
        return
    
    '''@QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.tableSecDegree.indexAt(button.pos()).row()
            self.tableSecDegree.removeRow(row)
        return'''
        
    def appendDataFromTextbox(self):
        self.fname, self.mi, self.lname, self.desiredcourse, self.date_a = self.getData()
        self.btnSubmit.clicked.connect(self.ClickSubmitButton)
        #numRows = self.tableSecDegree.rowCount()
        labels = ['fname','mi','lname','desiredcourse','remarks','dateadmission'] 
        
        qtable_df = self.write_qtable_to_df(self.tableSecDegree) 
        #datalist = [] #empty list
        for idx, row in qtable_df.iterrows(): 
            mylist = [row.FirstName, row.MI, row.LastName, row.DesiredCourse, row.Remarks]
                
            l = mylist+[self.date_a]
            self.lista.append(l)
        
        zippedlist = list(self.lista)
        print(zippedlist)
        df = pd.DataFrame(zippedlist, columns = labels )  
       # insert the CSV file
        df.to_csv(os.path.join(path,r'secDegreeApplicantsInfo.csv'), index = False )
        return df
    
    def ClickSubmitButton(self):
        self.fname, self.mi, self.lname, self.desiredcourse, self.date_a = self.getData()
        print(self.fname, self.mi, self.lname, self.desiredcourse, self.Remarks)
        self.addRow()
        QMessageBox.information(self, "SUBMITTED", 'You can view your record now.')
        return
    
    def ClickSearchButton(self):
        self.DataSearch()
        return
    
    def ClickUpdateButton(self): 
        self.appendDataFromTextbox()
        self.DataUpdate()
        return
        
    def ClickDeleteButton(self):
        self.DataDelete()
        return
    
    def getData(self):
        #assigning the variable names of the ObjectNames from the GUI
        #for printing the data in csv file
        fname = self.txtFName.text()
        mi = self.txtMI.text()
        lname = self.txtLName.text()
        desiredcourse = self.cmbCourses.currentText()
        date_a =  datetime.now()
        self.DateAdmission.setDate(date_a)
        
        if self.chkboxTOR.isChecked() and self.chkboxGoodMoral.isChecked() and self.chkbox12X2.isChecked() and self.chkboxTF400.isChecked() or self.chkboxTF300.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        date_a = self.DateAdmission.text()
        
        return fname, mi, lname, desiredcourse, date_a
    
    '''def remove(self): #row
        self.rows =  self.tableSecDegree.selectionModel().selectedRows()
        for r in self.rows:
            self.tableSecDegree.removeRow(r.rows())
        #self.select = self.selection.currentRowChanged()
        #self.selected = self.tableSecDegree.selectedItems()
        #self.tableSecDegree.removeRow(self.tableSecDegree.currentRow())
        return'''
        
    def addRow(self):
        self.fname, self.mi, self.lname, self.desiredcourse, self.date_a = self.getData()
        # Creates an empty row at bottom of table
        numRows = self.tableSecDegree.rowCount()
         
        self.tableSecDegree.insertRow(numRows)
        # Prints info/text to the intemInfo Table row
        self.tableSecDegree.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.fname))
        self.tableSecDegree.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.mi))
        self.tableSecDegree.setItem(numRows, 2, QtWidgets.QTableWidgetItem(self.lname))
        self.tableSecDegree.setItem(numRows, 3, QtWidgets.QTableWidgetItem(self.desiredcourse))
        self.tableSecDegree.setItem(numRows, 4, QtWidgets.QTableWidgetItem(self.Remarks))
      
        self.tableSecDegree.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableSecDegree.resizeRowsToContents()
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
        selectQuery = "SELECT * FROM tbl_secdegree"
        cur = con.cursor()
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
    
        for row in record:
            if search ==  str(row[1]):
                self.txtFName.setText(row[1])
                self.txtMI.setText(row[2])
                self.txtLName.setText(row[3])
                self.course = row[4]
                self.cmbCourses.setCurrentText(str(self.course))
                self.date_a = row[5]
                date_a =  datetime.now()
                self.DateAdmission.setDate(date_a)
                #self.DateAdmission.text(str(self.date_a))
                if row[6]== "Requirements are complete.\nQualified to enroll!":
                    self.chkboxTOR.setChecked(True) 
                    self.chkboxGoodMoral.setChecked(True)
                    self.chkbox12X2.setChecked(True)
                    if row[4]== "(BSIT) Bachelor of Science in Information Technology" or "(BSHM) Bachelor of Science in Hospitality Management" or "(AB-ELs) Bachelor of Arts in English Language Studies" or "(AB-Lit) Bachelor of Arts in Literature" or "(BIT-GT) Bachelor in Industrial Technology major in Garments Technology" or "(BIT-AT) Bachelor in Industrial Technology major in Automotive Technology" or "(BIT-CT) Bachelor in Industrial Technology major in Computer  Technology" or "(BIT-DT) Bachelor in Industrial Technology major in Drafting  Technology" or "(BIT-ET) Bachelor in Industrial Technology major in Electronics Technology":
                        self.chkboxTF300.setChecked(True)
                    else:
                        self.chkboxTF400.setChecked(True)
                    QMessageBox.information(self, "NOTICE","Your requirements are already complete.")
                else:
                    self.chkboxTOR.setChecked(False) 
                    self.chkboxGoodMoral.setChecked(False)
                    self.chkbox12X2.setChecked(False)
                    if row[4]=="(BSIT) Bachelor of Science in Information Technology" or "(BSHM) Bachelor of Science in Hospitality Management" or "(AB-ELs) Bachelor of Arts in English Language Studies" or "(AB-Lit) Bachelor of Arts in Literature" or "(BIT-GT) Bachelor in Industrial Technology major in Garments Technology" or "(BIT-AT) Bachelor in Industrial Technology major in Automotive Technology" or "(BIT-CT) Bachelor in Industrial Technology major in Computer  Technology" or "(BIT-DT) Bachelor in Industrial Technology major in Drafting  Technology" or "(BIT-ET) Bachelor in Industrial Technology major in Electronics Technology":
                        self.chkboxTF300.setChecked(False)
                    else:
                        self.chkboxTF400.setChecked(False)
                    QMessageBox.information(self, "NOTICE","Your requirements are incomplete. Please comply first.")
                break
        else:
            QMessageBox.information(self,"NOTICE","Search doesn't match any first name!")    
        
        con.commit()
        cur.close()
        #return record
    
    def DataUpdate(self):
        con = getConnection()
        name1 = self.txtMI.text()
        name2 = self.txtLName.text()
        course = self.cmbCourses.currentText()
        date_a =  datetime.now()
        self.DateAdmission.setDate(date_a)
        date_a = self.DateAdmission.text()
        if self.chkboxTOR.isChecked() and self.chkboxGoodMoral.isChecked() and self.chkbox12X2.isChecked():
            if self.chkboxTF400.isChecked() or self.chkboxTF300.isChecked():
                self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
        
        selectQuery = "Update tbl_secdegree SET mi = %s, lname = %s, desiredcourse = %s, dateadmission = %s, remarks = %s WHERE fname = %s" 
        search = str(self.txtSearch.text())
        equivalent = (name1, name2, course, date_a, self.Remarks, search)
        cur = con.cursor()
        cur.execute(selectQuery, equivalent)
        if self.chkboxTOR.isChecked() and self.chkboxGoodMoral.isChecked() and self.chkbox12X2.isChecked() and self.chkboxTF400.isChecked() or self.chkboxTF300.isChecked():
                QMessageBox.information(self, "RECORD UPDATED","You had successfully updated your record.\nPlease proceed at the Registrar Office to fully enroll. Thank you!")
        else:
            QMessageBox.information(self, "RECORD UPDATED","You had successfully updated your record.\nPlease complete your requirements first to proceed at the Registrar Office. Thank you!")
        
        self.ClearData()
        self.clickClearAll()
        self.txtSearch.setText('')
        con.commit()
        cur.close()
        return
    
    def DataDelete(self):
        cur = con.cursor()
        selectQuery = "SELECT * FROM tbl_secdegree"
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
         
        for row in record:
            if search ==  str(row[1]):
                buttonReply = QMessageBox.question(self, 'DELETE RECORD', "Are you sure to delete your record?", QMessageBox.Yes , QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql_Delete_query = """Delete from tbl_secdegree where fname = %s"""
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
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = secondDegreeWindowController()
    window.show()
    sys.exit(app.exec_())
