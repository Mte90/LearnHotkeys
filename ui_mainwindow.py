# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/LearnHotkeys/mainwindow.ui'
#
# Created: Fri Apr 27 00:00:58 2012
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
        MainWindow.resize(500, 247)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 263))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.question = QtGui.QLabel(self.centralWidget)
        self.question.setGeometry(QtCore.QRect(10, 40, 481, 51))
        self.question.setText(_fromUtf8(""))
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setObjectName(_fromUtf8("question"))
        self.hotkeys_program = QtGui.QLabel(self.centralWidget)
        self.hotkeys_program.setGeometry(QtCore.QRect(10, 10, 371, 16))
        self.hotkeys_program.setText(_fromUtf8(""))
        self.hotkeys_program.setObjectName(_fromUtf8("hotkeys_program"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 481, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.result = QtGui.QLabel(self.groupBox)
        self.result.setGeometry(QtCore.QRect(10, 80, 351, 16))
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        self.newQuestionButton = QtGui.QPushButton(self.groupBox)
        self.newQuestionButton.setGeometry(QtCore.QRect(370, 80, 97, 23))
        self.newQuestionButton.setObjectName(_fromUtf8("newQuestionButton"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 461, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.openDef = QtGui.QPushButton(self.centralWidget)
        self.openDef.setGeometry(QtCore.QRect(10, 220, 481, 23))
        self.openDef.setObjectName(_fromUtf8("openDef"))
        self.openCS = QtGui.QPushButton(self.centralWidget)
        self.openCS.setGeometry(QtCore.QRect(400, 10, 97, 23))
        self.openCS.setObjectName(_fromUtf8("openCS"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LearnHotkeys", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "HotKeys", None, QtGui.QApplication.UnicodeUTF8))
        self.newQuestionButton.setText(QtGui.QApplication.translate("MainWindow", "New Question", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.openDef.setText(QtGui.QApplication.translate("MainWindow", "Change Definition File", None, QtGui.QApplication.UnicodeUTF8))
        self.openCS.setText(QtGui.QApplication.translate("MainWindow", "CheatSheet", None, QtGui.QApplication.UnicodeUTF8))

