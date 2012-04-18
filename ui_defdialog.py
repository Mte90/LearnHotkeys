# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/LearnHotkeys/defdialog.ui'
#
# Created: Wed Apr 18 23:51:08 2012
#      by: PyQt4 UI code generator 4.9.1
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
        DefDialog.resize(400, 300)
        self.pushApply = QtGui.QPushButton(DefDialog)
        self.pushApply.setGeometry(QtCore.QRect(290, 270, 97, 23))
        self.pushApply.setObjectName(_fromUtf8("pushApply"))
        self.groupBox = QtGui.QGroupBox(DefDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboDef = QtGui.QComboBox(self.groupBox)
        self.comboDef.setGeometry(QtCore.QRect(20, 50, 331, 22))
        self.comboDef.setObjectName(_fromUtf8("comboDef"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.labelDef = QtGui.QLabel(self.groupBox)
        self.labelDef.setGeometry(QtCore.QRect(20, 80, 161, 21))
        self.labelDef.setText(_fromUtf8(""))
        self.labelDef.setObjectName(_fromUtf8("labelDef"))
        self.label = QtGui.QLabel(DefDialog)
        self.label.setGeometry(QtCore.QRect(140, 170, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(DefDialog)
        QtCore.QMetaObject.connectSlotsByName(DefDialog)

    def retranslateUi(self, DefDialog):
        DefDialog.setWindowTitle(QtGui.QApplication.translate("DefDialog", "Choose Definition", None, QtGui.QApplication.UnicodeUTF8))
        self.pushApply.setText(QtGui.QApplication.translate("DefDialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DefDialog", "Definition File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DefDialog", "Choose definition file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DefDialog", "Work in progress", None, QtGui.QApplication.UnicodeUTF8))

