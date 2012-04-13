#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import * 
import sys, os
from ui_defdialog import Ui_DefDialog

class DefWindow ( QDialog , Ui_DefDialog):

	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_DefDialog()
		self.ui.setupUi( self )
		self.show()
		#self.connect(self, SIGNAL("lastWindowClosed()"), self.exit )
