# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:56:13 2020

@author: Ma. Consuelo Entoma #BSIT-2B
"""

import sys
import os  #,re
import connectionUtility
from connectionUtility import getConnection 
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox
#from PyQt5.QtGui import QIcon, QPixmap
from transfereesGUI import Ui_TransfereeStudent
from transfereeModel import transfereesModel
import pandas as pd
path = 'D:/DOCU/Partial_Course_Admission_System/PartialCourseAdmission' # <-- NOTE: Set & edit folder path here from your D: drive where this project folder is placed.
con = getConnection()

class transfereesWindowController(QtWidgets.QWidget,Ui_TransfereeStudent):
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
        self.btnUpdate.clicked.connect(self.ClickUpdateButton)
        self.btnDelete.clicked.connect(self.ClickDeleteButton)
        self.btnClear.clicked.connect(self.clickClearAll)
        self.btnClearSearch.clicked.connect(self.clickClearAll)
        self.btnSearch.setIcon(QtGui.QIcon('image/icons8_Search_30px_1.png'))
        self.btnSearch.setIconSize(QtCore.QSize(50,50))
        self.btnImage.setIcon(QtGui.QIcon('image/transferee.jpg'))
        self.btnImage.setIconSize(QtCore.QSize(200,200))
        
    def ClickAddButton(self):
        self.appendDataFromTextbox()
        self.holder = transfereesModel()
        self.holder.insertStudentData()
        if self.checkBox1x1.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxTOR.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxGoodM.isChecked() or self.checkBoxNCAE.isChecked():
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
        self.txtPrevSchool.setText('')
        self.cmbCourse.setCurrentText('Select Course')
        self.checkBox1x1.setChecked(False)
        self.checkBoxNSO.setChecked(False)
        self.checkBoxTOR.setChecked(False)
        self.checkBox2x2.setChecked(False)
        self.checkBoxGoodM.setChecked(False)
        self.checkBoxNCAE.setChecked(False)
        self.tableTransferee.clearContents() 
        self.tableTransferee.model().removeRows(0, self.tableTransferee.rowCount())
        self.tableTransferee.setRowCount(0)
        self.tableTransferee.reset()
        return
     
    def clickClearAll(self):
        self.cmbCourse.setCurrentText('Select Course')
        return
    
    '''@QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.tableTransferee.indexAt(button.pos()).row()
            self.tableTransferee.removeRow(row)'''
    
    def appendDataFromTextbox(self):
        self.firstname, self.mi, self.lastname, self.previousschool, self.desiredcourse = self.getData()
        self.btnSubmit.clicked.connect(self.ClickSubmitButton)
        #numRows = self.itemTable.rowCount()
        labels = ['firstname','mi','lastname','previousschool','remarks','desiredcourse']
        
        qtable_df = self.write_qtable_to_df(self.tableTransferee) 
        #datalist = [] #empty list
        for idx, row in qtable_df.iterrows(): 
            mylist = [row.FirstName, row.MI, row.LastName, row.PreviousSchool, row.Remarks]
                
            l = mylist+[self.desiredcourse]
            self.lista.append(l)
        
        zippedlist = list(self.lista)
        print(zippedlist)
        df = pd.DataFrame(zippedlist, columns = labels )  
       # insert the CSV file
        df.to_csv(os.path.join(path,r'transfereesInfo.csv'), index = False)
        return df
    
    def ClickSubmitButton(self):
        self.firstname, self.mi, self.lastname, self.previousschool, self.desiredcourse = self.getData()
        print(self.firstname, self.mi, self.lastname, self.previousschool, self.desiredcourse, self.Remarks)
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
        firstname = self.txtFName.text()
        mi = self.txtMI.text()
        lastname = self.txtLName.text()
        previousschool = self.txtPrevSchool.text()
        desiredcourse = self.cmbCourse.currentText()
        
        if self.checkBox1x1.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxTOR.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxGoodM.isChecked() or self.checkBoxNCAE.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        return firstname, mi, lastname, previousschool, desiredcourse
    
    
    def addRow(self):
        self.firstname, self.mi, self.lastname, self.previousschool, self.desiredcourse = self.getData()
        # Creates an empty row at bottom of table
        numRows = self.tableTransferee.rowCount()
         
        self.tableTransferee.insertRow(numRows)
        # Adds info/text to the row
        self.tableTransferee.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.firstname))
        self.tableTransferee.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.mi))
        self.tableTransferee.setItem(numRows, 2, QtWidgets.QTableWidgetItem(self.lastname))
        self.tableTransferee.setItem(numRows, 3, QtWidgets.QTableWidgetItem(self.previousschool))
        self.tableTransferee.setItem(numRows, 4, QtWidgets.QTableWidgetItem(self.desiredcourse))
        self.tableTransferee.setItem(numRows, 5, QtWidgets.QTableWidgetItem(self.Remarks))
      
        self.tableTransferee.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableTransferee.resizeRowsToContents()
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
        selectQuery = "SELECT * FROM tbl_transferees"
        cur = con.cursor()
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
        
        for row in record:
            if search ==  str(row[1]):
                self.txtFName.setText(row[1])
                self.txtMI.setText(row[2])
                self.txtLName.setText(row[3])
                self.txtPrevSchool.setText(row[4])
                self.cmb = row[5]
                self.cmbCourse.setCurrentText(str(self.cmb))
                if row[6]== "Requirements are complete.\nQualified to enroll!":
                    self.checkBox1x1.setChecked(True) 
                    self.checkBoxNSO.setChecked(True)
                    self.checkBoxTOR.setChecked(True)
                    self.checkBox2x2.setChecked(True)
                    self.checkBoxGoodM.setChecked(True)
                    self.checkBoxNCAE.setChecked(True)
                    QMessageBox.information(self, "NOTICE","Your requirements are already complete.")
                else:
                    self.checkBox1x1.setChecked(False) 
                    self.checkBoxNSO.setChecked(False)
                    self.checkBoxTOR.setChecked(False)
                    self.checkBox2x2.setChecked(False)
                    self.checkBoxGoodM.setChecked(False)
                    self.checkBoxNCAE.setChecked(False)
                    QMessageBox.information(self, "NOTICE","Your requirements are incomplete. Please comply first.")  
                break
        else:
            QMessageBox.information(self,"NOTICE","Search doesn't match any first name!")    
        
        con.commit()
        cur.close()
        #return record
    
    def DataDelete(self):
        cur = con.cursor()
        selectQuery = "SELECT * FROM tbl_transferees"
        cur.execute(selectQuery)
        record = cur.fetchall()
        search = self.txtSearch.text()
         
        for row in record:
            if search ==  str(row[1]):
                buttonReply = QMessageBox.question(self, 'DELETE RECORD', "Are you sure to delete your record?", QMessageBox.Yes , QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    sql_Delete_query = """Delete from tbl_transferees where firstname = %s"""
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
        r2 = self.txtMI.text()
        r3 = self.txtLName.text()
        r4 = self.txtPrevSchool.text()
        r5 = self.cmbCourse.currentText()
        if self.checkBox1x1.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxTOR.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxGoodM.isChecked() or self.checkBoxNCAE.isChecked():
            self.Remarks = "Requirements are complete.\nQualified to enroll!"
        else:
            self.Remarks = "Incomplete Requirements.\nUnqualified to enroll!"
            
        selectQuery = "Update tbl_transferees SET mi = %s, lastname = %s, previousschool = %s, desiredcourse = %s, remarks = %s WHERE firstname = %s" 
        search = str(self.txtSearch.text())
        equivalent = (r2, r3, r4, r5, self.Remarks, search)
        cur = con.cursor()
        cur.execute(selectQuery, equivalent)
        
        if self.checkBox1x1.isChecked() and self.checkBoxNSO.isChecked() and self.checkBoxTOR.isChecked() and self.checkBox2x2.isChecked() and self.checkBoxGoodM.isChecked() or self.checkBoxNCAE.isChecked():
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
    window = transfereesWindowController()
    window.show()
    sys.exit(app.exec_())

