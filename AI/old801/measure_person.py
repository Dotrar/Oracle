#extract and find measurement
import cv2
import numpy as np
import time
import math
#load images

def nop(x):
	pass

img_ref_rgb = cv2.imread('ref.jpg')
img_pos_rgb = cv2.imread('pos.jpg')
foregBGR = cv2.resize(img_pos_rgb,(480,360))
backgBGR = cv2.resize(img_ref_rgb,(480,360))

foreg = cv2.cvtColor(foregBGR,cv2.COLOR_BGR2HSV)
backg = cv2.cvtColor(backgBGR,cv2.COLOR_BGR2HSV)
diff = cv2.absdiff(backg,foreg)

thresh = 10
ret,fmask = cv2.threshold(diff,thresh,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)
fmask = cv2.erode(fmask,kernel,iterations = 1)
fmask = cv2.dilate(fmask,kernel,iterations = 2)


res = cv2.cvtColor(cv2.bitwise_and(foreg,fmask),cv2.COLOR_HSV2BGR)

#cv2.imshow('diff',diff)
#cv2.imshow('denoised',cv2.fastNlMeansDenoising(diff,None,10,5,5))
#cv2.imshow('foreground',foreg)
cv2.imshow('result',res)


#blob some data
params = cv2.SimpleBlobDetector_Params()
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = False

detector = cv2.SimpleBlobDetector_create(params)

ffmask = cv2.cvtColor(fmask,cv2.COLOR_BGR2GRAY)
print(np.shape(ffmask))

kp = detector.detect(fmask)
print(kp)
img = cv2.drawKeypoints(foregBGR,kp,np.array([]),(0,0,255),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

im2, contours, hierarchy = cv2.findContours(ffmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

d = len(contours)
print('nc:',d)

font = cv2.FONT_HERSHEY_SIMPLEX
for k in kp:
	img = cv2.putText(img,'blob',(int(k.pt[0]),int(k.pt[1])),font,1,(0,0,255),2,cv2.LINE_AA)

#select the right blob

kx,ky = kp[0].pt


best = 0
bestdist = 100000

for i in range(d):
	cv2.drawContours(img,contours,i,(0,255,0),1)
	img = cv2.putText(img,'c{}'.format(i),(contours[i][0][0][0],contours[i][0][0][1]),
	                                       font,1,(0,255,0),1,cv2.LINE_AA)
	
	#select the best contour
	x,y = contours[i][0][0]
	dist = (kx-x)**2 + (ky-y)**2
	print(dist)
	if dist < bestdist:
		bestdist = dist
		best = i

print('best',i,bestdist)
#select the best contor

rect = cv2.boundingRect(contours[best])
cv2.rectangle(img,rect[0:2],(rect[0]+rect[2],rect[1]+rect[3]),(255,0,0),1)

cv2.drawContours(img,contours,best,(255,0,0),2)
cv2.imshow('blob, contours and rect',img)


#now try to measure the person.
#imagesize = 480,360
cx,cy = 240,180

deg = math.degrees(math.atan2(ky-cy,kx - cx))+90 #plus 90 for final rot

x,y,w,h = rect
pers = foregBGR[y:y+h,x:x+w]
rows,cols = h,w
M = cv2.getRotationMatrix2D((cols/2,rows/2),deg,0.7)
pers = cv2.warpAffine(pers,M,(cols,rows))
pers = cv2.resize(pers,(480,360))

cv2.imshow('person',pers)


#height extraction



cv2.waitKey(0)