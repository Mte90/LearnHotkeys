#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import * 
import sys, os
from ui_cheatsheet import Ui_CSDialog

class CSWindow ( QDialog , Ui_CSDialog):
	
	settings = QSettings('settings.ini', QSettings.IniFormat)
	settings.setFallbacksEnabled(False)
	html_cs = ""
	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_CSDialog()
		self.ui.setupUi( self )
		self.ui.saveButton.clicked.connect(self.saveHTML)
		self.ui.closeButton.clicked.connect(self.accept)
		self.loadHotkeys()
		self.show()

	def loadHotkeys(self):
		fname = './hotkeys/'+self.settings.value('file_name_default').toString()
		dom = QDomDocument()
		error = None
		fh = None
		self.html_cs = "<style>table{ font-family: 'PT Sans','DejaVu Sans','Bitstream Vera Sans',Verdana,sans-serif;}</style><table><tr style='font-weight:bold'><td>Action</td><td>HotKey</td></tr>"
		try:
			fh = QFile(fname)
			if not fh.open(QIODevice.ReadOnly):
				raise IOError, unicode(fh.errorString())
			if not dom.setContent(fh):
				raise ValueError, "could not parse XML"
		except (IOError, OSError, ValueError), e:
			error = "Failed to import: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error
		root = dom.documentElement()
		if not root.hasAttribute('fileversion'):
			QMessageBox.information(self.window(), "LearnHotkeys","The file {} is not an LearnHotkeys definition file." % self.settings.value('file_name_default').toString())
			return False
		child = root.firstChildElement('hotkey')
		while not child.isNull():
			self.html_cs += "<tr><td>%s</td><td>%s</td></tr>" % (child.firstChildElement('question').text(),child.firstChildElement('key').text())
			child = child.nextSiblingElement('hotkey')
		self.html_cs += "</table>"
		self.ui.csView.setHtml(self.html_cs)
		
	def saveHTML(self):
	  filename =  QFileDialog.getSaveFileName(self, 'Save HTML CheatSheet', self.settings.value('file_name_default').toString()+'.html')
	  fname = open(filename, 'w')
	  fname.write(self.html_cs)
	  fname.close() 
