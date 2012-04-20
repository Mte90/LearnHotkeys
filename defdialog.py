#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import * 
import sys, os
from ui_defdialog import Ui_DefDialog

class DefWindow ( QDialog , Ui_DefDialog):
	
	def_file = []
	settings = QSettings('settings.ini', QSettings.IniFormat)
	settings.setFallbacksEnabled(False)
	
	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_DefDialog()
		self.ui.setupUi( self )
		self.show()
		for root, dirs, files in os.walk('./hotkeys'):
			for name in files:
			   filename = os.path.join(root, name)
			   self.ui.comboDef.addItem(os.path.basename(filename))
			   #self.def_file.append(filename)
		print self.settings.value('file_name_default').toString()
		if self.ui.comboDef.findText(self.settings.value('file_name_default').toString()) != -1:
			self.ui.comboDef.setCurrentIndex(self.ui.comboDef.findText(self.settings.value('file_name_default').toString()) )
		self.ui.comboDef.currentIndexChanged.connect(self.comboDefChanged)
		
	def comboDefChanged(self, file):
		self.settings.setValue("file_name_default", self.ui.comboDef.currentText())

