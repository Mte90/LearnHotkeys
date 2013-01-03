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
    questions_edit = []
    fileInUse = ''

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Editor()
        self.ui.setupUi( self )
        for root, dirs, files in os.walk(self.hotkeys_path):
            files.sort()
            for name in files:
                filename = os.path.join(root, name)
                if os.path.basename(filename) != 'list':
                    self.ui.comboHotkeys.addItem(os.path.basename(filename))
        self.ui.comboHotkeys.currentIndexChanged.connect(self.loadHotkeys)
        self.ui.pushSave.clicked.connect(self.saveXML)
        self.ui.listQuestion.currentRowChanged.connect(self.loadQuestion)
        self.ui.question.textChanged.connect(self.markEdited)
        self.ui.hotkey.textChanged.connect(self.markEdited)
        self.ui.pushNewQuestion.pressed.connect(self.newField)
        self.ui.pushNew.pressed.connect(self.newFile)
        self.loadHotkeys()
        self.show()

    def loadHotkeys(self):
        self.fileInUse = self.ui.comboHotkeys.currentText()
        fname = self.hotkeys_folder+self.fileInUse
        dom = QDomDocument()
        error = None
        fh = None
        self.questions[:] = []
        self.hotkeys[:] = []
        self.ui.listQuestion.clear()
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
        self.ui.listQuestion.setCurrentRow(0)
        self.loadQuestion(0)

    def loadQuestion(self,item):
        self.ui.question.textChanged.disconnect()
        self.ui.hotkey.textChanged.disconnect()
        try:
           self.ui.question.setText(self.questions[item])
           self.ui.hotkey.setText(self.hotkeys[item])
        except IndexError:
            pass
        self.ui.question.textChanged.connect(self.markEdited)
        self.ui.hotkey.textChanged.connect(self.markEdited)

    def markEdited(self):
        a = self.ui.listQuestion.currentRow()
        if a == -1:
            a = 0
        item_selected = self.ui.listQuestion.item(a)
        try:
           self.questions_edit[a]
        except IndexError:
            if item_selected != None:
                self.questions_edit.append(a)
        if self.ui.question.toPlainText() != self.questions[a]:
            item_selected.setText(str(a+1) + ' - '+ self.ui.question.toPlainText()+ '*')
        self.questions[a] = self.ui.question.toPlainText()
        self.hotkeys[a] = self.ui.hotkey.text()

    def newField(self):
        number_question = self.ui.listQuestion.count()+1
        self.ui.listQuestion.addItem(str(number_question) + ' - ')
        self.questions.append('')
        self.hotkeys.append('')
        self.loadQuestion(number_question-1)
        self.ui.listQuestion.setCurrentRow(number_question-1)
        self.ui.totalQuestion.setText('Total question: '+str(number_question))

    def newFile(self):
        self.questions[:] = []
        self.hotkeys[:] = []
        self.ui.listQuestion.clear()
        self.ui.description.setText('')
        self.ui.webSite.setText('')
        self.ui.fileVersion.setText('')
        self.ui.softwareName.setText('')
        self.ui.softwareVersion.setText('')
        text, ok = QInputDialog.getText(self, 'New Question Hotkey File', 'Insert the name of the file:', QLineEdit.Normal, '.xml')
        if (ok):
             self.fileInUse = text
             self.saveXML()
             self.ui.comboHotkeys.currentIndexChanged.disconnect()
             self.ui.comboHotkeys.addItem(text)
             self.ui.comboHotkeys.setCurrentIndex(self.ui.comboHotkeys.count()-1)
             self.ui.comboHotkeys.currentIndexChanged.connect(self.loadHotkeys)
             self.newField()

    def saveXML(self):
        fname = self.hotkeys_folder+self.fileInUse
        error = None
        fh = None
        try:
            fh = QFile(fname)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError, unicode(fh.errorString())
            stream = QTextStream(fh)
            stream.setCodec('UTF-8')
            stream << ("<?xml version='1.0' encoding='UTF-8' ?>\n"
                       '<software fileversion="%s" softwareversion="%s" def="%s" software="%s" softwaresite="%s">' % (
                        self.ui.fileVersion.text(),
                        self.ui.softwareVersion.text(),
                        self.ui.description.text(),
                        self.ui.softwareName.text(),
                        self.ui.webSite.text()))
            stream <<  ("\n")
            for key, value_ in enumerate(self.questions):
                stream << ("\t<hotkey>\n"
                           "\t\t<question>%s</question>\n"
                           "\t\t<key>%s</key>\n"
                           "\t</hotkey>\n" % (value_,self.hotkeys[key]))
            stream << "</software>\n"
        except (IOError, OSError), e:
            error = "Failed to export: %s" % e
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                print error