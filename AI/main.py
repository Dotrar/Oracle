#!/usr/bin/python3

import cv2
import numpy as np


file = r'C:\Users\Dre West\Documents\GitHub\Oracle\AI\1530762287_1.jpg'

img = cv2.imread(file)

cv2.imshow('image',img)

cv2.waitKey()

#contours
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
kernel = np.ones((5,5),np.uint8)
gray = cv2.erode(gray,kernel,iterations = 1)
gray = cv2.dilate(gray,kernel,iterations = 2)
## (2) Threshold
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

_, cnts, _ = cv2.findContours(threshed,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea)
for c,cnt in enumerate(cnts):
	pass
	cv2.drawContours(img,[cnt],-1,c,-1)

cv2.imshow('thread',threshed)
#blobs
params = cv2.SimpleBlobDetector_Params()
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = False


is_v2 = cv2.__version__.startswith("2.")
if is_v2:
	print('cv version 2')
	detector = cv2.SimpleBlobDetector(params)
else:
	print('cv version 3')
	detector = cv2.SimpleBlobDetector_create(params)


keypoints = detector.detect(threshed)



img_with_keypoints = cv2.drawKeypoints(img,keypoints,np.array([]),(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('keypoints',img_with_keypoints)
cv2.waitKey()

