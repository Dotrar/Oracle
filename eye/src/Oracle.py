from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *

import threading
import time

import boto3
from io import BytesIO
import numpy as np
import json

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
        self._img = []
        self._flagged = False

        #aws services
        #self.sage = boto3.Session().client(service_name='sagemaker-runtime')


    def handle_cameras(self):
        '''
            for i in range(3):
               c = cv2.VideoCapture(x)
               _,img = cam.read()
               del c
               _,j = cv2.imencode('.jpg',img)

            return image_array
        '''
        pass

    def get_model_response(self):
        '''
        resp = self.sage.invoke_endpoint(
            EndpointName='Oracle-endpoint',
            ContentType='application/x-image',
            Body=bytearray(self._img[0]))

        res = resp['Body'].read()
        res = json.loads(res.decode('utf-8'))
        '''
        pass

    def upload_new(self,code):
        print('upload new passed with',code)
        pass

    # ---------------------------------------------- slots

    @pyqtSlot()
    def capture(self):      # returns a list of possible options, [] [1] [1,2,3]
        print('calling capture')
        #capture is called so we shouldn't already cancel out of it
        self._cancel = False
        # ------------------------- define thread
        def thread():
            print('Simulating a timed process in a thread')
            time.sleep(1)
    
            # img_array = self.handle_cameras()
            # resp = self.get_model_response()

            if not self._cancel:
                #self._recentimg = img_array
                self._response = ['AA1234', 'BB2345', 'CC3456', 'DD4567']
                self.responseReceived.emit(self._response)
        # -----------------------------------------
        threading.Thread(target=thread).start()



    @pyqtSlot()
    def cancel(self):
        self._cancel = True

    @pyqtSlot(str)
    def confirm(self,code):

        if self._flagged:
            # send to s3 input bucket
            self.upload_new(code)
        else:
            pass

        #clear everything and restart
        #qml will handle the screen transition
        self._recentimg = []
        self._response = []
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
