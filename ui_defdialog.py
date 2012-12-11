# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/LearnHotkeys/defdialog.ui'
#
# Created: Tue Dec 11 15:34:11 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DefDialog(object):
    def setupUi(self, DefDialog):
        DefDialog.setObjectName(_fromUtf8("DefDialog"))
        DefDialog.resize(392, 309)
        DefDialog.setModal(True)
        self.pushApply = QtGui.QPushButton(DefDialog)
        self.pushApply.setGeometry(QtCore.QRect(280, 280, 97, 23))
        self.pushApply.setObjectName(_fromUtf8("pushApply"))
        self.groupBox = QtGui.QGroupBox(DefDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboDef = QtGui.QComboBox(self.groupBox)
        self.comboDef.setGeometry(QtCore.QRect(20, 30, 331, 21))
        self.comboDef.setObjectName(_fromUtf8("comboDef"))
        self.labelDef = QtGui.QLabel(self.groupBox)
        self.labelDef.setGeometry(QtCore.QRect(20, 60, 331, 51))
        self.labelDef.setText(_fromUtf8(""))
        self.labelDef.setObjectName(_fromUtf8("labelDef"))
        self.pushUpdate = QtGui.QPushButton(DefDialog)
        self.pushUpdate.setGeometry(QtCore.QRect(180, 280, 94, 25))
        self.pushUpdate.setObjectName(_fromUtf8("pushUpdate"))
        self.pushDownload = QtGui.QPushButton(DefDialog)
        self.pushDownload.setGeometry(QtCore.QRect(80, 280, 94, 25))
        self.pushDownload.setObjectName(_fromUtf8("pushDownload"))
        self.groupBox_2 = QtGui.QGroupBox(DefDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 140, 371, 131))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listUpdate = QtGui.QListView(self.groupBox_2)
        self.listUpdate.setGeometry(QtCore.QRect(0, 30, 371, 101))
        self.listUpdate.setProperty("showDropIndicator", False)
        self.listUpdate.setObjectName(_fromUtf8("listUpdate"))

        self.retranslateUi(DefDialog)
        QtCore.QMetaObject.connectSlotsByName(DefDialog)

    def retranslateUi(self, DefDialog):
        DefDialog.setWindowTitle(QtGui.QApplication.translate("DefDialog", "Choose Definition", None, QtGui.QApplication.UnicodeUTF8))
        self.pushApply.setText(QtGui.QApplication.translate("DefDialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DefDialog", "Choose Definition File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushUpdate.setText(QtGui.QApplication.translate("DefDialog", "Update List", None, QtGui.QApplication.UnicodeUTF8))
        self.pushDownload.setText(QtGui.QApplication.translate("DefDialog", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DefDialog", "Update", None, QtGui.QApplication.UnicodeUTF8))

