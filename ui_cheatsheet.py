# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/LearnHotkeys/cheatsheet.ui'
#
# Created: Tue Dec 18 18:02:39 2012
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
        self.gridLayout = QtGui.QGridLayout(CSDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.csView = QtWebKit.QWebView(CSDialog)
        self.csView.setAcceptDrops(False)
        self.csView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.csView.setObjectName(_fromUtf8("csView"))
        self.gridLayout.addWidget(self.csView, 0, 0, 1, 3)
        self.themeChooser = QtGui.QComboBox(CSDialog)
        self.themeChooser.setObjectName(_fromUtf8("themeChooser"))
        self.gridLayout.addWidget(self.themeChooser, 1, 0, 1, 1)
        self.saveButton = QtGui.QPushButton(CSDialog)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        self.closeButton = QtGui.QPushButton(CSDialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 1, 2, 1, 1)

        self.retranslateUi(CSDialog)
        QtCore.QMetaObject.connectSlotsByName(CSDialog)

    def retranslateUi(self, CSDialog):
        CSDialog.setWindowTitle(QtGui.QApplication.translate("CSDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("CSDialog", "Save .HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("CSDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
