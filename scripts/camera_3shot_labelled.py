#!/usr/bin/python3
#initial_camera

import time
import cv2
import numpy as np
import time
from appJar import gui
import sys, os

try:
    os.chdir('../images')
except Exception as e:
    print("quitting: can't move to expected dir,",e)
    exit()

product_code = str(input('product: ')).upper()

try:
    os.mkdir(product_code)
except FileExistsError as e:
    pass
os.chdir(product_code)


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

while True:
    input('reposition and take shot')

    for x in range(3):
        t = int(time.time())
        cam = cv2.VideoCapture(x)
        _,img = cam.read()
        del cam
        cv2.imwrite('{}_{}.jpg'.format(t,x),img)
