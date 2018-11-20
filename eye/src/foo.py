
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *


class Foo(QObject):
    progressChanged = pyqtSignal(int)
    
    def __init__(self, *args, **kwags):
        QObject.__init__(self, *args, **kwags)
        self._progress = 10

    @pyqtSlot()
    def run_bar(self):
        print('hello world')

    @pyqtProperty(int, notify=progressChanged)
    def progress(self):
        return self._progress


    @pyqtSlot(int)
    def updateProgress(self, value):
        if self._progress == value:
            return
        self._progress = value
        self.progressChanged.emit(self._progress)

    @pyqtSlot()
    def bar(self):
        print ('hellow dre')

