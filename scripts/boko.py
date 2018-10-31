#!/usr/bin/python3

import boto3
from appJar import gui
import cv2
from io import BytesIO
import numpy as np
import json

import sys, os

object_cat = ['PA3566','PS0804','PP0800','PT3020']

desc  = {
    'PA3566': 'gold right angle RCA',
    'PT3020': 'gold binding post thing',
    'PS0804': 'D9 Solder socket',
    'PP0800': 'D9 Solder plug'
}


for i in range(3):
	print('camera',i)
	cam = cv2.VideoCapture(i)
	while True:
		_,img = cam.read()
		
		cv2.imshow('Camera {} : '.format(i), img)
		
		if cv2.waitKey(1) == 27:
			break
	
	del cam #remember to free up resources
	cv2.destroyAllWindows()




runtime = boto3.Session().client(service_name='sagemaker-runtime')


def scan(button):


    if button == 'next':

        app.setTabbedFrameSelectedTab('device','scan')

    if button == 'scan':
        max = 0
        print('-'*30)
        for x in range(3):
            cam = cv2.VideoCapture(x)
            _,img = cam.read()
            del cam

            jpg_img = cv2.imencode('.jpg',img)

            response = runtime.invoke_endpoint(
                EndpointName='oracle-ep-2018-10-15-05-14-16',
                ContentType='application/x-image',
                Body=bytearray(jpg_img[1])
                )

            result = response['Body'].read()
            result = json.loads(result.decode('utf-8'))
            print(result)

            m = np.max(result)
            print("camera {} has max {}".format(x,m))
            print("max is still {}".format(max))
            if m > max:
                print('new leader')
                max = m
                am = np.argmax(result)
                print(am)
                p = object_cat[am]
                item_d = '{} ({}%)'.format(p,int(max*100))
                print(item_d)
                print(desc[p])

                app.setLabel('item',item_d)
                app.setLabel('desc',desc[p])

        app.setTabbedFrameSelectedTab('device','display')


app = gui("Oracle","fullscreen")

app.startTabbedFrame('device')

app.startTab('scan')
app.addButton('scan',scan)
app.stopTab()

app.startTab('display')
app.addLabel('item')
app.addLabel('desc')
app.addButton('next',scan)
app.stopTab()

app.setFont(size=32,family="Verdana")

app.stopTabbedFrame()

app.go()
