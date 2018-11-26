from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *

import threading
import time


class Oracle(QObject):

    responseReceived = pyqtSignal(list)
    responseChanged  = pyqtSignal(list)
    selectionChanged = pyqtSignal(str)

    # ---------------------------------------------- internals
    def __init__(self, *args, **kwags):
        QObject.__init__(self, *args, **kwags)
        self._value = ''
        self._select = ''
        self._response = []

    def handle_cameras(self):
        pass

    def get_model_response(self):
        pass

    def upload_new(self):
        pass

    # ---------------------------------------------- slots

    @pyqtSlot()
    def capture(self):      # returns a list of possible options, [] [1] [1,2,3]

        #capture is called so we shouldn't already cancel out of it
        self._cancel = False

        # ------------------------- define thread
        def thread():
            print('Simulating a timed process in a thread')
            time.sleep(1)

            if not self._cancel:
                self._response = ['AA1234', 'BB2345', 'CC3456', 'DD4567']
                self.responseReceived.emit(self._response)

        # -----------------------------------------

        threading.Thread(target=thread).start()

    @pyqtSlot()
    def cancel(self):
        self._cancel = True

    @pyqtSlot(str)
    def offer_correction(self,code):
        pass

    @pyqtSlot(str)
    def select(self,code):
        self._selection = code
        self.selectionChanged.emit(self._selection)

    # ----------------------------------------------- properties
    @pyqtProperty(list, notify = responseChanged)
    def response(self):
        return self._response

    @pyqtProperty(str, notify = selectionChanged)
    def selection(self):
        return self._selection
