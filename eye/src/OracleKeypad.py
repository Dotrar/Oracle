from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *


class OracleKeypad(QObject):

    columnsChanged = pyqtSignal(int)
    keypadChanged = pyqtSignal(list)
    valueChanged = pyqtSignal(str)
    finished = pyqtSignal(bool)
   

    def __init__(self, *args, **kwags):
        QObject.__init__(self, *args, **kwags)
        self.productListing = [x.strip() for x in open('productListing').readlines()]
        self._value = ''
        self.buildKeypad()

    def buildKeypad(self):
        if self._value == '':
            #initial stage, so load letters:
            self._keypad = [x[:2].upper() for x in self.productListing] 

        else: #something there, so load limited numbers:
            self._keypad = [x for x in range(10)]


    # ---------------------------------------------- slots

    @pyqtSlot(str)
    def pressed(self,value):
        self._value += str(value) #ensure string
        if len(self._value) == 6:
            self.finished.emit(True)

        self.buildKeypad()

        self.keypadChanged.emit(self._keypad)

    
    @pyqtSlot()
    def backspace(self):
        self._value = ''
        self.buildKeypad()
        self.keypadChanged.emit(self._keypad)



    # ----------------------------------------------- properties
    @pyqtProperty(list, notify=keypadChanged)
    def model(self):
        return self._keypad

    @pyqtProperty(str, notify=keypadChanged)
    def value(self):
        return self._value

    @pyqtProperty(int, notify=columnsChanged)
    def columns(self):
        return self._columns

'''
    @pyqtSlot(int)
    def updateProgress(self, value):
        if self._progress == value:
            return
        self._progress = value
        self.progressChanged.emit(self._progress)
'''
