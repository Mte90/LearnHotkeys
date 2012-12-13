#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
import sys, os
from ui_editor import Ui_Editor

class EditorWindow ( QDialog , Ui_Editor):

	settings = QSettings()
	settings.setFallbacksEnabled(False)
	hotkeys_path = "./hotkeys"
	hotkeys_folder = hotkeys_path+'/'

	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_Editor()
		self.ui.setupUi( self )
		for root, dirs, files in os.walk(self.hotkeys_path):
			for name in files:
				filename = os.path.join(root, name)
				self.ui.comboHotkeys.addItem(os.path.basename(filename))
		self.ui.comboHotkeys.currentIndexChanged.connect(self.loadHotkeys)
		self.loadHotkeys()
		self.show()

	def loadHotkeys(self):
		fname = self.hotkeys_folder+self.ui.comboHotkeys.currentText()
		dom = QDomDocument()
		error = None
		fh = None
		try:
			fh = QFile(fname)
			if not fh.open(QIODevice.ReadOnly):
				print(IOError, unicode(fh.errorString()))
			if not dom.setContent(fh):
				print(ValueError, "could not parse XML")
		except (IOError, OSError, ValueError) as e:
			error = "Failed to import: {0}".format(e)
		finally:
			if fh is not None:
				fh.close()
			if error is not None:
				return False, error
		root = dom.documentElement()
		if not root.hasAttribute('fileversion'):
			QMessageBox.information(self.window(), "LearnHotkeys","The file %s is not an LearnHotkeys definition file." % self.ui.comboHotkeys.currentText())
			return False
		self.ui.description.setText(root.attribute('def'))
		self.ui.webSite.setText(root.attribute('softwaresite'))
		self.ui.fileVersion.setText(root.attribute('fileversion'))
		self.ui.softwareName.setText(root.attribute('software'))
		self.ui.softwareVersion.setText(root.attribute('softwareversion'))
		count_child = 0
		child = root.firstChildElement('hotkey')
		while not child.isNull():
			#self.html_cs += "\n<tr><td>%s</td><td>%s</td></tr>" % (child.firstChildElement('question').text(),child.firstChildElement('key').text())
			count_child = count_child+1
			child = child.nextSiblingElement('hotkey')
		self.ui.totalQuestion.setText('Total question: '+str(count_child))
		#self.html_cs += "</table></body></html>"
		#if sys.version_info < (3, 0):
			#self.ui.csView.setHtml((self.html_style % self.get_file_content(self.theme_folder+self.settings.value('theme').toString()))+self.html_thead+self.html_cs)
		#else:
			#self.ui.csView.setHtml((self.html_style % self.get_file_content(self.theme_folder+self.settings.value('theme')))+self.html_thead+self.html_cs)


	#def saveHTML(self):
		#if sys.version_info < (3, 0):
			#filename =  QFileDialog.getSaveFileName(self, 'Save HTML CheatSheet', self.settings.value('file_name_default').toString()[:-4]+'.html')
			#fname = open(filename, 'w')
			#html = (self.html_style% self.get_file_content(self.theme_folder+self.settings.value('theme').toString()))+self.html_def+self.html_thead+self.html_cs
		#else:
			#filename =  QFileDialog.getSaveFileName(self, 'Save HTML CheatSheet', self.settings.value('file_name_default')[:-4]+'.html')
			#fname = open(filename, 'w')
			#html = (self.html_style% self.get_file_content(self.theme_folder+self.settings.value('theme')))+self.html_def+self.html_thead+self.html_cs
		#fname.write(html.toUtf8()+"\n")
		#fname.close()

