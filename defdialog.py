#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
import sys, os, urllib
from ui_defdialog import Ui_DefDialog

class DefWindow ( QDialog , Ui_DefDialog):

	hotkeys_path = "./hotkeys"
	hotkeys_folder = hotkeys_path+'/'
	settings = QSettings()
	settings.setFallbacksEnabled(False)

	def __init__ ( self, parent = None ):
		QDialog.__init__( self, parent )
		self.ui = Ui_DefDialog()
		self.ui.setupUi( self )
		self.ui.pushApply.clicked.connect(self.saveConfig)
		self.ui.pushUpdate.clicked.connect(self.downloadList)
		self.show()
		for root, dirs, files in os.walk(self.hotkeys_path):
			for name in files:
				filename = os.path.join(root, name)
				self.ui.comboDef.addItem(os.path.basename(filename))
		if sys.version_info < (3, 0):
			try:
				if self.ui.comboDef.findText(self.settings.value('file_name_default').toString) != -1:
					self.ui.comboDef.setCurrentIndex(self.ui.comboDef.findText(self.settings.value('file_name_default').toString()))
			except:
				pass
		elif self.ui.comboDef.findText(self.settings.value('file_name_default')) != -1:
			self.ui.comboDef.setCurrentIndex(self.ui.comboDef.findText(self.settings.value('file_name_default')))
		self.ui.comboDef.currentIndexChanged.connect(self.comboDefChanged)
		self.comboDefChanged()
		self.parseList()

	def comboDefChanged(self):
		fname = self.hotkeys_folder+self.ui.comboDef.currentText()
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
			QMessageBox.information(self.window(), "LearnHotkeys","The file {} is not an LearnHotkeys definition file." % self.ui.comboDef.currentText())
			return False
		self.ui.labelDef.setText('<font style="font-weight:bold"> %s - %s<font><br>%s <br><a href="%s">%s</a>' \
		% (root.attribute('software'),root.attribute('softwareversion'),root.attribute('def'),root.attribute('softwaresite'),root.attribute('softwaresite')))

	def saveConfig(self):
		self.settings.setValue("file_name_default", self.ui.comboDef.currentText())
		self.accept()

	def downloadList(self):
		urllib.urlretrieve('https://raw.github.com/Mte90/LearnHotkeys/master/hotkeys/list', self.hotkeys_folder+'list')

	def parseList(self):
		model = QStandardItemModel()
		logfile = open(self.hotkeys_folder+'list', "r").readlines()
		for line in logfile:
			line = line.replace('\n','').split('|')
			item = QStandardItem(line[1] + ' - Syntax ' + line[2] + ' - ' + 'Software ' + line[3])
			item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
			item.setData(QVariant(Qt.Checked), Qt.CheckStateRole)
			model.appendRow(item)
		self.ui.listUpdate.setModel(model)
		pass
