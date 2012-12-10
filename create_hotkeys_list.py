#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtXml import *
import sys, os

hotkeys_path = "./hotkeys"
hotkeys_folder = hotkeys_path+'/'
list_hotkeys = ''

for root, dirs, files in os.walk(hotkeys_path):
	for name in files:
		if name.endswith('.xml'):
			fname = os.path.join(root, name)
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
					print(error)
			if not dom.documentElement().hasAttribute('fileversion'):
				print("LearnHotkeys","The file {} is not an LearnHotkeys definition file." % fname)
			list_hotkeys = list_hotkeys + name + "|" + dom.documentElement().attribute('software') + "|" + dom.documentElement().attribute('softwareversion') + "|" + dom.documentElement().attribute('def')+'\n'

f = open(hotkeys_folder + 'list','w+')
f.write(list_hotkeys)
f.close()