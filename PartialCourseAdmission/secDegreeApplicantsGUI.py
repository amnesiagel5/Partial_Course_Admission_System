# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\DOCU\Partial_Course_Admission_System\PartialCourseAdmission\UI\secDegreeApplicants.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecDegree(object):
    def setupUi(self, SecDegree):
        SecDegree.setObjectName("SecDegree")
        SecDegree.setEnabled(True)
        SecDegree.resize(1211, 620)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        SecDegree.setFont(font)
        SecDegree.setAcceptDrops(False)
        self.labelSecdegreeTitle = QtWidgets.QLabel(SecDegree)
        self.labelSecdegreeTitle.setGeometry(QtCore.QRect(390, 20, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelSecdegreeTitle.setFont(font)
        self.labelSecdegreeTitle.setObjectName("labelSecdegreeTitle")
        self.labelFName = QtWidgets.QLabel(SecDegree)
        self.labelFName.setGeometry(QtCore.QRect(70, 120, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelFName.setFont(font)
        self.labelFName.setObjectName("labelFName")
        self.txtFName = QtWidgets.QLineEdit(SecDegree)
        self.txtFName.setGeometry(QtCore.QRect(170, 120, 341, 21))
        self.txtFName.setObjectName("txtFName")
        self.btnSubmit = QtWidgets.QPushButton(SecDegree)
        self.btnSubmit.setEnabled(True)
        self.btnSubmit.setGeometry(QtCore.QRect(320, 490, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setCheckable(False)
        self.btnSubmit.setObjectName("btnSubmit")
        self.labelReq = QtWidgets.QLabel(SecDegree)
        self.labelReq.setGeometry(QtCore.QRect(40, 280, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelReq.setFont(font)
        self.labelReq.setObjectName("labelReq")
        self.labelCourse = QtWidgets.QLabel(SecDegree)
        self.labelCourse.setGeometry(QtCore.QRect(40, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelCourse.setFont(font)
        self.labelCourse.setObjectName("labelCourse")
        self.btnClear = QtWidgets.QPushButton(SecDegree)
        self.btnClear.setGeometry(QtCore.QRect(230, 490, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnCancel = QtWidgets.QPushButton(SecDegree)
        self.btnCancel.setGeometry(QtCore.QRect(600, 570, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.cmbCourses = QtWidgets.QComboBox(SecDegree)
        self.cmbCourses.setGeometry(QtCore.QRect(170, 240, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cmbCourses.setFont(font)
        self.cmbCourses.setObjectName("cmbCourses")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.cmbCourses.addItem("")
        self.labelMI = QtWidgets.QLabel(SecDegree)
        self.labelMI.setGeometry(QtCore.QRect(60, 150, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.labelMI.setFont(font)
        self.labelMI.setObjectName("labelMI")
        self.labelLName = QtWidgets.QLabel(SecDegree)
        self.labelLName.setGeometry(QtCore.QRect(80, 180, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelLName.setFont(font)
        self.labelLName.setObjectName("labelLName")
        self.txtMI = QtWidgets.QLineEdit(SecDegree)
        self.txtMI.setGeometry(QtCore.QRect(170, 150, 341, 20))
        self.txtMI.setObjectName("txtMI")
        self.txtLName = QtWidgets.QLineEdit(SecDegree)
        self.txtLName.setGeometry(QtCore.QRect(170, 180, 341, 20))
        self.txtLName.setObjectName("txtLName")
        self.chkboxTOR = QtWidgets.QCheckBox(SecDegree)
        self.chkboxTOR.setEnabled(True)
        self.chkboxTOR.setGeometry(QtCore.QRect(180, 310, 441, 17))
        self.chkboxTOR.setObjectName("chkboxTOR")
        self.chkboxGoodMoral = QtWidgets.QCheckBox(SecDegree)
        self.chkboxGoodMoral.setGeometry(QtCore.QRect(180, 330, 451, 17))
        self.chkboxGoodMoral.setObjectName("chkboxGoodMoral")
        self.chkbox12X2 = QtWidgets.QCheckBox(SecDegree)
        self.chkbox12X2.setGeometry(QtCore.QRect(180, 350, 431, 17))
        self.chkbox12X2.setObjectName("chkbox12X2")
        self.labelFee = QtWidgets.QLabel(SecDegree)
        self.labelFee.setGeometry(QtCore.QRect(180, 380, 81, 21))
        self.labelFee.setObjectName("labelFee")
        self.chkboxTF400 = QtWidgets.QCheckBox(SecDegree)
        self.chkboxTF400.setGeometry(QtCore.QRect(210, 420, 301, 17))
        self.chkboxTF400.setObjectName("chkboxTF400")
        self.chkboxTF300 = QtWidgets.QCheckBox(SecDegree)
        self.chkboxTF300.setGeometry(QtCore.QRect(210, 440, 291, 17))
        self.chkboxTF300.setObjectName("chkboxTF300")
        self.tableSecDegree = QtWidgets.QTableWidget(SecDegree)
        self.tableSecDegree.setEnabled(True)
        self.tableSecDegree.setGeometry(QtCore.QRect(660, 120, 521, 171))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tableSecDegree.setFont(font)
        self.tableSecDegree.setObjectName("tableSecDegree")
        self.tableSecDegree.setColumnCount(5)
        self.tableSecDegree.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSecDegree.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSecDegree.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSecDegree.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSecDegree.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSecDegree.setHorizontalHeaderItem(4, item)
        self.btnAdd = QtWidgets.QPushButton(SecDegree)
        self.btnAdd.setEnabled(True)
        self.btnAdd.setGeometry(QtCore.QRect(880, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnUpdate = QtWidgets.QPushButton(SecDegree)
        self.btnUpdate.setGeometry(QtCore.QRect(690, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnDelete = QtWidgets.QPushButton(SecDegree)
        self.btnDelete.setGeometry(QtCore.QRect(690, 490, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnDelete.setFont(font)
        self.btnDelete.setObjectName("btnDelete")
        self.txtSearch = QtWidgets.QLineEdit(SecDegree)
        self.txtSearch.setGeometry(QtCore.QRect(690, 400, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.txtSearch.setFont(font)
        self.txtSearch.setText("")
        self.txtSearch.setReadOnly(False)
        self.txtSearch.setObjectName("txtSearch")
        self.line_6 = QtWidgets.QFrame(SecDegree)
        self.line_6.setGeometry(QtCore.QRect(10, 90, 20, 451))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(SecDegree)
        self.line_7.setGeometry(QtCore.QRect(630, 90, 20, 451))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(SecDegree)
        self.line_8.setGeometry(QtCore.QRect(20, 530, 621, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(SecDegree)
        self.line_9.setGeometry(QtCore.QRect(170, 80, 471, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(SecDegree)
        self.line_10.setGeometry(QtCore.QRect(20, 80, 21, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.labelInfo = QtWidgets.QLabel(SecDegree)
        self.labelInfo.setGeometry(QtCore.QRect(40, 80, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setItalic(True)
        self.labelInfo.setFont(font)
        self.labelInfo.setObjectName("labelInfo")
        self.labelRead = QtWidgets.QLabel(SecDegree)
        self.labelRead.setGeometry(QtCore.QRect(670, 81, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setItalic(True)
        self.labelRead.setFont(font)
        self.labelRead.setObjectName("labelRead")
        self.line_11 = QtWidgets.QFrame(SecDegree)
        self.line_11.setGeometry(QtCore.QRect(640, 100, 20, 241))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(SecDegree)
        self.line_12.setGeometry(QtCore.QRect(650, 90, 21, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(SecDegree)
        self.line_13.setGeometry(QtCore.QRect(920, 90, 271, 20))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(SecDegree)
        self.line_14.setGeometry(QtCore.QRect(1180, 100, 20, 241))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(SecDegree)
        self.line_15.setGeometry(QtCore.QRect(650, 330, 541, 20))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.labelDate = QtWidgets.QLabel(SecDegree)
        self.labelDate.setGeometry(QtCore.QRect(80, 210, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.DateAdmission = QtWidgets.QDateEdit(SecDegree)
        self.DateAdmission.setGeometry(QtCore.QRect(170, 210, 341, 22))
        self.DateAdmission.setCalendarPopup(True)
        self.DateAdmission.setDate(QtCore.QDate(2020, 5, 1))
        self.DateAdmission.setObjectName("DateAdmission")
        self.line_16 = QtWidgets.QFrame(SecDegree)
        self.line_16.setGeometry(QtCore.QRect(640, 370, 20, 171))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(SecDegree)
        self.line_17.setGeometry(QtCore.QRect(960, 370, 20, 171))
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(SecDegree)
        self.line_18.setGeometry(QtCore.QRect(650, 530, 321, 20))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.labelsSUD = QtWidgets.QLabel(SecDegree)
        self.labelsSUD.setGeometry(QtCore.QRect(670, 350, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setItalic(True)
        self.labelsSUD.setFont(font)
        self.labelsSUD.setObjectName("labelsSUD")
        self.line_19 = QtWidgets.QFrame(SecDegree)
        self.line_19.setGeometry(QtCore.QRect(650, 360, 21, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(SecDegree)
        self.line_20.setGeometry(QtCore.QRect(950, 360, 21, 20))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.btnSearch = QtWidgets.QPushButton(SecDegree)
        self.btnSearch.setGeometry(QtCore.QRect(890, 400, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSearch.setFont(font)
        self.btnSearch.setText("")
        self.btnSearch.setObjectName("btnSearch")
        self.btnClearSearch = QtWidgets.QPushButton(SecDegree)
        self.btnClearSearch.setGeometry(QtCore.QRect(810, 450, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClearSearch.setFont(font)
        self.btnClearSearch.setObjectName("btnClearSearch")
        self.btnImage = QtWidgets.QPushButton(SecDegree)
        self.btnImage.setGeometry(QtCore.QRect(980, 370, 211, 171))
        self.btnImage.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.btnImage.setText("")
        self.btnImage.setAutoDefault(False)
        self.btnImage.setDefault(False)
        self.btnImage.setFlat(True)
        self.btnImage.setObjectName("btnImage")

        self.retranslateUi(SecDegree)
        self.btnClear.clicked.connect(self.txtFName.clear)
        self.btnClear.clicked.connect(self.txtMI.clear)
        self.btnClear.clicked.connect(self.txtLName.clear)
        self.btnClear.clicked.connect(self.cmbCourses.clearEditText)
        self.btnClear.clicked['bool'].connect(self.chkboxTOR.setChecked)
        self.btnClear.clicked['bool'].connect(self.chkboxGoodMoral.setChecked)
        self.btnClear.clicked['bool'].connect(self.chkbox12X2.setChecked)
        self.btnClear.clicked['bool'].connect(self.chkboxTF400.setChecked)
        self.btnClear.clicked['bool'].connect(self.chkboxTF300.setChecked)
        self.btnCancel.clicked.connect(SecDegree.close)
        self.btnDelete.clicked.connect(self.tableSecDegree.reset)
        self.btnClearSearch.clicked.connect(self.txtSearch.clear)
        self.btnClearSearch.clicked.connect(self.txtFName.clear)
        self.btnClearSearch.clicked.connect(self.txtMI.clear)
        self.btnClearSearch.clicked.connect(self.txtLName.clear)
        self.btnClearSearch.clicked.connect(self.cmbCourses.clearEditText)
        self.btnClearSearch.clicked['bool'].connect(self.chkboxTOR.setChecked)
        self.btnClearSearch.clicked['bool'].connect(self.chkboxGoodMoral.setChecked)
        self.btnClearSearch.clicked['bool'].connect(self.chkbox12X2.setChecked)
        self.btnClearSearch.clicked['bool'].connect(self.chkboxTF400.setChecked)
        self.btnClearSearch.clicked['bool'].connect(self.chkboxTF300.setChecked)
        QtCore.QMetaObject.connectSlotsByName(SecDegree)

    def retranslateUi(self, SecDegree):
        _translate = QtCore.QCoreApplication.translate
        SecDegree.setWindowTitle(_translate("SecDegree", "Second Degree/Courser Applicant"))
        self.labelSecdegreeTitle.setText(_translate("SecDegree", "Partial Admission for Second Degree Applicant"))
        self.labelFName.setText(_translate("SecDegree", "First Name :"))
        self.btnSubmit.setText(_translate("SecDegree", "Submit"))
        self.labelReq.setText(_translate("SecDegree", "Checking Requirements : "))
        self.labelCourse.setText(_translate("SecDegree", "Desired  Course : "))
        self.btnClear.setText(_translate("SecDegree", "Clear"))
        self.btnCancel.setText(_translate("SecDegree", "Cancel"))
        self.cmbCourses.setItemText(0, _translate("SecDegree", "Available Courses"))
        self.cmbCourses.setItemText(1, _translate("SecDegree", "(BSA) Bachelor of Science in Agriculture major in Animal Science"))
        self.cmbCourses.setItemText(2, _translate("SecDegree", "(BSA) Bachelor of Science in Agriculture major in Horticulture"))
        self.cmbCourses.setItemText(3, _translate("SecDegree", "(BSA) Bachelor of Science in Agriculture major in Agronomy"))
        self.cmbCourses.setItemText(4, _translate("SecDegree", "(BSA) Bachelor of Science in Agriculture major in Crop Production"))
        self.cmbCourses.setItemText(5, _translate("SecDegree", "(BSA) Bachelor of Science in Agriculture major in Agricultural Economics"))
        self.cmbCourses.setItemText(6, _translate("SecDegree", "(BSF) Bachelor of Science in Forestry"))
        self.cmbCourses.setItemText(7, _translate("SecDegree", "(BSIE) Bachelor of Science in Industrial Engineering"))
        self.cmbCourses.setItemText(8, _translate("SecDegree", "(BSIT) Bachelor of Science in Information Technology"))
        self.cmbCourses.setItemText(9, _translate("SecDegree", "(BSHM) Bachelor of Science in Hospitality Management"))
        self.cmbCourses.setItemText(10, _translate("SecDegree", "(BEED) Bachelor of Elementary Education"))
        self.cmbCourses.setItemText(11, _translate("SecDegree", "(BTLEd) Bachelor of Technology and Livelihood Education major in Home Economics"))
        self.cmbCourses.setItemText(12, _translate("SecDegree", "(BSED-Math) Bachelor of Secondary Education major in Math"))
        self.cmbCourses.setItemText(13, _translate("SecDegree", "(AB-ELs) Bachelor of Arts in English Language Studies"))
        self.cmbCourses.setItemText(14, _translate("SecDegree", "(AB-Lit) Bachelor of Arts in Literature"))
        self.cmbCourses.setItemText(15, _translate("SecDegree", "(BIT-GT) Bachelor in Industrial Technology major in Garments Technology"))
        self.cmbCourses.setItemText(16, _translate("SecDegree", "(BIT-AT) Bachelor in Industrial Technology major in Automotive Technology"))
        self.cmbCourses.setItemText(17, _translate("SecDegree", "(BIT-CT) Bachelor in Industrial Technology major in Computer Technology"))
        self.cmbCourses.setItemText(18, _translate("SecDegree", "(BIT-DT) Bachelor in Industrial Technology major in Drafting Technology"))
        self.cmbCourses.setItemText(19, _translate("SecDegree", "(BIT-ET) Bachelor in Industrial Technology major in Electronics Technology"))
        self.labelMI.setText(_translate("SecDegree", "Middle Initial:"))
        self.labelLName.setText(_translate("SecDegree", "Last Name:"))
        self.chkboxTOR.setText(_translate("SecDegree", "• Transcript of Records (TOR) with Remarks: For Evaluation (Original)"))
        self.chkboxGoodMoral.setText(_translate("SecDegree", "• Certificate of Good Moral Character from last school attended (Original)"))
        self.chkbox12X2.setText(_translate("SecDegree", "• 1 pc. recent 2X2 colored picture with white background and nametag"))
        self.labelFee.setText(_translate("SecDegree", "Testing Fee:"))
        self.chkboxTF400.setText(_translate("SecDegree", "  • Php 400.00 for board/courses programs"))
        self.chkboxTF300.setText(_translate("SecDegree", "  • Php 300.00 for non-board/courses programs"))
        item = self.tableSecDegree.horizontalHeaderItem(0)
        item.setText(_translate("SecDegree", "FirstName"))
        item = self.tableSecDegree.horizontalHeaderItem(1)
        item.setText(_translate("SecDegree", "MI"))
        item = self.tableSecDegree.horizontalHeaderItem(2)
        item.setText(_translate("SecDegree", "LastName"))
        item = self.tableSecDegree.horizontalHeaderItem(3)
        item.setText(_translate("SecDegree", "DesiredCourse"))
        item = self.tableSecDegree.horizontalHeaderItem(4)
        item.setText(_translate("SecDegree", "Remarks"))
        self.btnAdd.setText(_translate("SecDegree", "Add Record"))
        self.btnUpdate.setText(_translate("SecDegree", "Update Record"))
        self.btnDelete.setText(_translate("SecDegree", "Delete Record"))
        self.txtSearch.setPlaceholderText(_translate("SecDegree", "Enter your First Name to Search"))
        self.labelInfo.setText(_translate("SecDegree", "Enter Information"))
        self.labelRead.setText(_translate("SecDegree", "Preview-Add Information/Record"))
        self.labelDate.setText(_translate("SecDegree", "Date Today:"))
        self.labelsSUD.setText(_translate("SecDegree", " Search-Update-Delete Existing Record"))
        self.btnClearSearch.setText(_translate("SecDegree", "Clear Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecDegree = QtWidgets.QWidget()
    ui = Ui_SecDegree()
    ui.setupUi(SecDegree)
    SecDegree.show()
    sys.exit(app.exec_())