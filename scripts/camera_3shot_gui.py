#!/usr/bin/python3
#initial_camera

import time
'''
assuming all goes well, this should be set up to run on the pi.

from which, the pi will manage 3 webcameras that are attached to it
and tell the user what to do.

'''

import cv2
import numpy as np
import time
from appJar import gui
import sys, os

SCREEN = "fullscreen" #"480x800"

imgs = []

def kp(button):
	app.set
	pass

def scan(button):
#open up webcameras, take a picture from each
	if button == 'return':
		app.setTabbedFrameSelectedTab('device','scan')
		return
	
	t = int(time.time())
	for x in range(3):
		cam = cv2.VideoCapture(x)
		_,img = cam.read()
	#cv2.imshow('cam {}'.format(x), img)
		del cam
	#imgs.append(img)
		cv2.imwrite('img/{}_{}.jpg'.format(t,x),img)

	dnum = len([x for x in os.listdir('img/') if os.path.isfile('img/'+str(x))])
	app.setLabel('number','{} of 3000'.format(dnum))

#start a gui

app = gui("Oracle",SCREEN)

app.startTabbedFrame('device')

app.startTab('scan')

app.addLabel('instruction','Place a part in and press scan')
app.addLabel('number','')
app.addButton('SCAN',scan)
app.setButtonBg('SCAN','green')
app.setButtonPadding('SCAN',[90,60])

app.stopTab()

app.startTab('write')

app.addButton('return',scan)
app.setButtonPadding('return',[90,60])
app.addLabel('change part, then return')
##add keypad entry
#app.setStretch("both")
#
#app.setSticky("nesw")
#app.addEntry('something',colspan=3)
#for idx,v in enumerate([7,8,9,4,5,6,1,2,3]):
#        app.addButton(str(v),kp,1+int((idx)/3),idx%3)
#app.addButton('0',kp,app.getRow(),0,colspan=2)
#app.addButton('Back',kp,app.getRow()-1,2)
#
app.stopTab()
app.stopTabbedFrame()


# configuration

#app.getEntryWidget('something').config(font="Times 62")
#app.setEntryMaxLength('something',4)
#app.setEntryWidth('something',10)

app.go()
