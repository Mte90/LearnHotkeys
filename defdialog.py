#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import * 
import sys, os
from ui_defdialog import Ui_DefDialog

class DefWindow ( QDialog , Ui_DefDialog):
	
	def_file = []
	
	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_DefDialog()
		self.ui.setupUi( self )
		self.show()
		for root, dirs, files in os.walk('./hotkeys'):
			for name in files:
			   filename = os.path.join(root, name)
			   self.ui.comboDef.addItem(filename)
			   #self.def_file.append(filename)

		#self.connect(self, SIGNAL("lastWindowClosed()"), self.exit )
