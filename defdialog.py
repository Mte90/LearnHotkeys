#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
import sys, os, urllib
from ui_defdialog import Ui_DefDialog

class DefWindow ( QDialog , Ui_DefDialog):

    hotkeys_path = "./hotkeys"
    hotkeys_folder = hotkeys_path+'/'
    settings = QSettings('Mte90','LearnHotkeys')
    settings.setFallbacksEnabled(False)

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent, Qt.CustomizeWindowHint)
        self.ui = Ui_DefDialog()
        self.ui.setupUi( self )
        self.ui.pushApply.clicked.connect(self.saveConfig)
        self.ui.pushUpdate.clicked.connect(self.downloadList)
        self.ui.pushDownload.clicked.connect(self.downloadSyntax)
        self.show()
        for root, dirs, files in os.walk(self.hotkeys_path):
            files.sort()
            for name in files:
                filename = os.path.join(root, name)
                if os.path.basename(filename) != 'list':
                    self.ui.comboDef.addItem(os.path.basename(filename))
        if sys.version_info < (3, 0):
            try:
                if self.ui.comboDef.findText(self.settings.value('file_name_default').toString()) != -1:
                    self.ui.comboDef.setCurrentIndex(self.ui.comboDef.findText(self.settings.value('file_name_default').toString()))
            except:
                pass
        elif self.ui.comboDef.findText(self.settings.value('file_name_default')) != -1:
            self.ui.comboDef.setCurrentIndex(self.ui.comboDef.findText(self.settings.value('file_name_default')))
        self.ui.comboDef.currentIndexChanged.connect(self.comboDefChanged)
        self.comboDefChanged()
        self.parseList()

    def comboDefChanged(self):
        root = self.syntaxParser(self.ui.comboDef.currentText())
        self.ui.labelDef.setText('<font style="font-weight:bold"> %s - %s<font><br>%s <br><a href="%s">%s</a>' \
        % (root.attribute('software'),root.attribute('softwareversion'),root.attribute('def'),root.attribute('softwaresite'),root.attribute('softwaresite')))

    def saveConfig(self):
        self.settings.setValue("file_name_default", self.ui.comboDef.currentText())
        self.accept()

    def downloadList(self):
        urllib.urlretrieve('https://raw.github.com/Mte90/LearnHotkeys/master/hotkeys/list', self.hotkeys_folder+'list')
        QMessageBox.information(self.window(), "LearnHotkeys","The file list has been updated.")
        self.parseList()

    def parseList(self):
        model = QStandardItemModel()
        logfile = open(self.hotkeys_folder+'list', "r").readlines()
        for line in logfile:
            line = line.replace('\n','').split('|')
            #check if syntax exist
            if os.path.exists(self.hotkeys_folder+line[0]):
                root = self.syntaxParser(line[0])
                temp = root.attribute('fileversion')
            else:
                temp = '0'

            if temp != line[2]:
                item = QStandardItem('New! ' + line[1] + ' - Syntax ' + line[2] + ' - ' + 'Software ' + line[3])
                item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled| Qt.ToolTip)
                item.setData(QVariant(Qt.Checked), Qt.CheckStateRole)
            else:
                item = QStandardItem(line[1] + ' - Syntax ' + line[2] + ' - ' + 'Software ' + line[3])
                item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled| Qt.ToolTip)
                item.setData(False, Qt.CheckStateRole)
            item.setToolTip(line[0])
            model.appendRow(item)
        self.ui.listUpdate.setModel(model)

    def downloadSyntax(self):
        #loop the item on list for download the update
        for index in range(self.ui.listUpdate.model().rowCount()):
            check_box = self.ui.listUpdate.model().item(index)
            state = check_box.checkState()
            file_name = str(check_box.toolTip())
            if state != False:
                urllib.urlretrieve('https://raw.github.com/Mte90/LearnHotkeys/master/hotkeys/'+file_name, self.hotkeys_folder+file_name)
                QMessageBox.information(self.window(), "LearnHotkeys","The file %s has been downloaded." % file_name)
        self.parseList()

    def syntaxParser(self,file):
        fname = self.hotkeys_folder+file
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
            QMessageBox.information(self.window(), "LearnHotkeys","The file %s is not an LearnHotkeys definition file." % file)
            return False
        return root