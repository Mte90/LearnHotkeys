# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/LearnHotkeys/mainwindow.ui'
#
# Created: Thu Apr 12 23:17:41 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 247)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(400, 263))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.question = QtGui.QLabel(self.centralWidget)
        self.question.setGeometry(QtCore.QRect(10, 40, 371, 51))
        self.question.setText(_fromUtf8(""))
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setObjectName(_fromUtf8("question"))
        self.hotkeys_program = QtGui.QLabel(self.centralWidget)
        self.hotkeys_program.setGeometry(QtCore.QRect(10, 10, 381, 16))
        self.hotkeys_program.setText(_fromUtf8(""))
        self.hotkeys_program.setObjectName(_fromUtf8("hotkeys_program"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 381, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 30, 101, 41))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(260, 30, 101, 41))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.result = QtGui.QLabel(self.groupBox)
        self.result.setGeometry(QtCore.QRect(10, 70, 241, 16))
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        self.newQuestionButton = QtGui.QPushButton(self.groupBox)
        self.newQuestionButton.setGeometry(QtCore.QRect(270, 70, 97, 23))
        self.newQuestionButton.setObjectName(_fromUtf8("newQuestionButton"))
        self.openDef = QtGui.QPushButton(self.centralWidget)
        self.openDef.setGeometry(QtCore.QRect(10, 220, 381, 23))
        self.openDef.setObjectName(_fromUtf8("openDef"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LearnHotkeys", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "HotKeys", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.newQuestionButton.setText(QtGui.QApplication.translate("MainWindow", "New Question", None, QtGui.QApplication.UnicodeUTF8))
        self.openDef.setText(QtGui.QApplication.translate("MainWindow", "Change Definition File", None, QtGui.QApplication.UnicodeUTF8))

