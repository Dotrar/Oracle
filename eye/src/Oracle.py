from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *


class Oracle(QObject):

    columnsChanged = pyqtSignal(int)
    keypadChanged = pyqtSignal(list)
    valueChanged = pyqtSignal(str)
    finished = pyqtSignal(bool)
   

    # ---------------------------------------------- internals
    def __init__(self, *args, **kwags):
        QObject.__init__(self, *args, **kwags)
        self._value = ''

    def handle_cameras(self):
        pass

    def get_model_response(self):
        pass

    def upload_new(self):
        pass

    # ---------------------------------------------- slots

    @pyqtSlot(list)
    def capture(self):      # returns a list of possible options, [] [1] [1,2,3]
        pass

    @pyqtSlot()
    def offer_correction(self,code):
        pass
        

    # ----------------------------------------------- properties
    @pyqtProperty(list, notify=keypadChanged)
    def model(self):
        return self._keypad

    @pyqtProperty(str, notify=keypadChanged)
    def value(self):
        return self._value

