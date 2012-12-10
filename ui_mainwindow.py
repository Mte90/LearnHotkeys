# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/LearnHotkeys/mainwindow.ui'
#
# Created: Tue Dec 11 00:20:15 2012
#      by: PyQt4 UI code generator 4.9.3
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
        MainWindow.resize(500, 259)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(540, 260))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 31))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.openCS = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openCS.sizePolicy().hasHeightForWidth())
        self.openCS.setSizePolicy(sizePolicy)
        self.openCS.setObjectName(_fromUtf8("openCS"))
        self.gridLayout.addWidget(self.openCS, 0, 1, 1, 1)
        self.hotkeys_program = QtGui.QLabel(self.gridLayoutWidget)
        self.hotkeys_program.setText(_fromUtf8(""))
        self.hotkeys_program.setObjectName(_fromUtf8("hotkeys_program"))
        self.gridLayout.addWidget(self.hotkeys_program, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 39, 482, 221))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.question = QtGui.QLabel(self.verticalLayoutWidget)
        self.question.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question.sizePolicy().hasHeightForWidth())
        self.question.setSizePolicy(sizePolicy)
        self.question.setMinimumSize(QtCore.QSize(480, 80))
        self.question.setText(_fromUtf8(""))
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setObjectName(_fromUtf8("question"))
        self.verticalLayout.addWidget(self.question)
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(480, 100))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.result = QtGui.QLabel(self.groupBox)
        self.result.setGeometry(QtCore.QRect(10, 70, 351, 16))
        self.result.setText(_fromUtf8(""))
        self.result.setObjectName(_fromUtf8("result"))
        self.newQuestionButton = QtGui.QPushButton(self.groupBox)
        self.newQuestionButton.setGeometry(QtCore.QRect(370, 70, 97, 23))
        self.newQuestionButton.setObjectName(_fromUtf8("newQuestionButton"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 461, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.openDef = QtGui.QPushButton(self.verticalLayoutWidget)
        self.openDef.setObjectName(_fromUtf8("openDef"))
        self.verticalLayout.addWidget(self.openDef)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LearnHotkeys", None, QtGui.QApplication.UnicodeUTF8))
        self.openCS.setText(QtGui.QApplication.translate("MainWindow", "CheatSheet", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "HotKeys", None, QtGui.QApplication.UnicodeUTF8))
        self.newQuestionButton.setText(QtGui.QApplication.translate("MainWindow", "New Question", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.openDef.setText(QtGui.QApplication.translate("MainWindow", "Change Definition File", None, QtGui.QApplication.UnicodeUTF8))

