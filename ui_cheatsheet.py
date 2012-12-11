# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/LearnHotkeys/cheatsheet.ui'
#
# Created: Tue Dec 11 11:54:33 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CSDialog(object):
    def setupUi(self, CSDialog):
        CSDialog.setObjectName(_fromUtf8("CSDialog"))
        CSDialog.resize(421, 371)
        CSDialog.setModal(True)
        self.csView = QtWebKit.QWebView(CSDialog)
        self.csView.setGeometry(QtCore.QRect(10, 10, 401, 321))
        self.csView.setAcceptDrops(False)
        self.csView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.csView.setObjectName(_fromUtf8("csView"))
        self.saveButton = QtGui.QPushButton(CSDialog)
        self.saveButton.setGeometry(QtCore.QRect(210, 340, 97, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.closeButton = QtGui.QPushButton(CSDialog)
        self.closeButton.setGeometry(QtCore.QRect(320, 340, 97, 23))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.themeChooser = QtGui.QComboBox(CSDialog)
        self.themeChooser.setGeometry(QtCore.QRect(10, 340, 191, 22))
        self.themeChooser.setObjectName(_fromUtf8("themeChooser"))

        self.retranslateUi(CSDialog)
        QtCore.QMetaObject.connectSlotsByName(CSDialog)

    def retranslateUi(self, CSDialog):
        CSDialog.setWindowTitle(QtGui.QApplication.translate("CSDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("CSDialog", "Save .HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("CSDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
