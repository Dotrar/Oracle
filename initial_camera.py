#initial_camera

'''
assuming all goes well, this should be set up to run on the pi.

from which, the pi will manage 3 webcameras that are attached to it
and tell the user what to do.

'''

import cv2
import numpy as np
import time
from appJar import gui

SCREEN = "480x800"

imgs = []

def kp(button):
	
	pass

def scan(button):
	#open up webcameras, take a picture from each


	for x in range(3):
		cam = cv2.VideoCapture(x)
		_,img = cam.read()
		#cv2.imshow('cam {}'.format(x), img)
		del cam
		imgs.append(img)
	
	app.setTabbedFrameSelectedTab('device','write')

#start a gui

app = gui("Oracle",SCREEN)

app.startTabbedFrame('device')

app.startTab('scan')

app.addLabel('instruction','Place a part in and press scan')
app.addButton('SCAN',scan)

app.stopTab()

app.startTab('write')

app.addEntry
#add keypad entry
app.setStretch("both")

app.setSticky("nesw")
app.addEntry('something',colspan=3)
for idx,v in enumerate([7,8,9,4,5,6,1,2,3]):
	app.addButton(str(v),kp,int(idx/3),idx%3)
app.addButton('0',kp,app.getRow(),0,colspan=2)
app.addButton('Back',kp,app.getRow()-1,2)

app.stopTab()
app.stopTabbedFrame()

app.go()