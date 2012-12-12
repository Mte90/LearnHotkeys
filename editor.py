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
		#self.ui.saveButton.clicked.connect(self.saveHTML)
		#self.ui.closeButton.clicked.connect(self.accept)
		#for root, dirs, files in os.walk(self.theme_path):
			#for name in files:
				#filename = os.path.join(root, name)
				#self.ui.themeChooser.addItem(os.path.basename(filename))

		#if sys.version_info < (3, 0):
			#if not self.settings.value('theme').toString():
				#self.saveConfig()
				#try:
					#if self.ui.themeChooser.findText(self.settings.value('theme').toString()) != -1:
						#self.ui.themeChooser.setCurrentIndex(self.ui.themeChooser.findText(self.settings.value('theme').toString()))
				#except:
					#pass
		#else:
			#if not self.settings.value('theme'):
				#self.saveConfig()
			#self.ui.themeChooser.setCurrentIndex(self.ui.themeChooser.findText(self.settings.value('theme')))
		#self.ui.themeChooser.currentIndexChanged.connect(self.saveConfig)
		#self.loadHotkeys()
		self.show()

	#def loadHotkeys(self):
		#if sys.version_info < (3, 0):
			#if self.settings.value('file_name_default').toString() != "":
				#fname = self.hotkeys_folder+self.settings.value('file_name_default').toString()
		#else:
			#if self.settings.value('file_name_default') != "":
				#fname = self.hotkeys_folder+self.settings.value('file_name_default')
		#dom = QDomDocument()
		#error = None
		#fh = None
		#try:
			#fh = QFile(fname)
			#if not fh.open(QIODevice.ReadOnly):
				#print(IOError, unicode(fh.errorString()))
			#if not dom.setContent(fh):
				#print(ValueError, "could not parse XML")
		#except (IOError, OSError, ValueError) as e:
			#error = "Failed to import: {0}".format(e)
		#finally:
			#if fh is not None:
				#fh.close()
			#if error is not None:
				#return False, error
		#root = dom.documentElement()
		#if not root.hasAttribute('fileversion'):
			#QMessageBox.information(self.window(), "LearnHotkeys","The file {} is not an LearnHotkeys definition file." % self.settings.value('file_name_default').toString())
			#return False
		#self.html_def += root.attribute('software')+" - "+root.attribute('softwareversion')+" - "+root.attribute('def')+"<br>\n<a href='"+root.attribute('softwaresite')+"'>" \
		#+root.attribute('softwaresite')+"</a><br> CheatSheet version: "+root.attribute('fileversion')+"<br><br>"
		#child = root.firstChildElement('hotkey')
		#while not child.isNull():
			#self.html_cs += "\n<tr><td>%s</td><td>%s</td></tr>" % (child.firstChildElement('question').text(),child.firstChildElement('key').text())
			#child = child.nextSiblingElement('hotkey')
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

	#def get_file_content(self,file):
		#f = open(file, 'r')
		#c = f.read()
		#f.close()
		#return c

	#def saveConfig(self):
		#self.settings.setValue("theme", self.ui.themeChooser.currentText())
		#if sys.version_info < (3, 0):
			#self.ui.csView.setHtml((self.html_style % self.get_file_content(self.theme_folder+self.settings.value('theme').toString()))+self.html_thead+self.html_cs)
		#else:
			#self.ui.csView.setHtml((self.html_style % self.get_file_content(self.theme_folder+self.settings.value('theme')))+self.html_thead+self.html_cs)
