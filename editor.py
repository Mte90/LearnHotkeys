#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
import os
from ui_editor import Ui_Editor

class EditorWindow ( QDialog , Ui_Editor):

    settings = QSettings()
    settings.setFallbacksEnabled(False)
    hotkeys_path = "./hotkeys"
    hotkeys_folder = hotkeys_path+'/'
    questions = []
    hotkeys = []
    item_previous = 2
    questions_edit = []

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Editor()
        self.ui.setupUi( self )
        for root, dirs, files in os.walk(self.hotkeys_path):
            for name in files:
                filename = os.path.join(root, name)
                self.ui.comboHotkeys.addItem(os.path.basename(filename))
        self.ui.comboHotkeys.currentIndexChanged.connect(self.loadHotkeys)
        self.ui.pushSave.clicked.connect(self.saveXML)
        self.ui.listQuestion.currentRowChanged.connect(self.loadQuestion)
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
            count_child += 1
            self.ui.listQuestion.addItem(str(count_child) + ' - '+ child.firstChildElement('question').text())
            self.questions.append(child.firstChildElement('question').text())
            self.hotkeys.append(child.firstChildElement('key').text())
            child = child.nextSiblingElement('hotkey')
        self.ui.totalQuestion.setText('Total question: '+str(count_child))
        self.ui.listQuestion.item(0).setSelected(True)
        self.loadQuestion(0)

    def loadQuestion(self,item):
        self.ui.question.textChanged.disconnect()
        self.ui.hotkey.textChanged.disconnect()
        self.ui.question.setText(self.questions[item])
        self.ui.hotkey.setText(self.hotkeys[item])
        self.item_previous = item
        self.ui.question.textChanged.connect(self.markEdited)
        self.ui.hotkey.textChanged.connect(self.markEdited)

    def markEdited(self):
            try:
                b=self.questions_edit.index(self.ui.listQuestion.currentRow())
            except ValueError:
                item_selected = self.ui.listQuestion.item(self.ui.listQuestion.currentRow())
                if item_selected != None:
                    item_selected.setText(item_selected.text() + '*')
                    self.questions_edit.append(self.ui.listQuestion.currentRow())

    def saveXML(self):
        pass
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

