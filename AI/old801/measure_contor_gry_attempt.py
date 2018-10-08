#extract and find measurement
import cv2
import numpy as np
import time
#load images

def nop(x):
	pass

img_ref_rgb = cv2.imread('ref.jpg',0)
img_pos_rgb = cv2.imread('pos.jpg',0)
foreg = cv2.resize(img_pos_rgb,(480,360))
backg = cv2.resize(img_ref_rgb,(480,360))

diff = cv2.absdiff(backg,foreg)

thresh = 10
ret,fmask = cv2.threshold(diff,thresh,255,cv2.THRESH_BINARY)
#fmask = cv2.adaptiveThreshold(diff,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,4)

kernel = np.ones((5,5),np.uint8)
fmask = cv2.erode(fmask,kernel,iterations = 2)
fmask = cv2.dilate(fmask,kernel,iterations = 5)


res = cv2.bitwise_and(foreg,fmask)

cv2.imshow('diff',diff)
#cv2.imshow('denoised',cv2.fastNlMeansDenoising(diff,None,10,5,5))
cv2.imshow('foreground',foreg)
cv2.imshow('result',res)


#blob some data
params = cv2.SimpleBlobDetector_Params()
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = False
params.filterByInertia = False
params.filterByArea = False

detector = cv2.SimpleBlobDetector_create(params)

print(np.shape(fmask))
kp = detector.detect(fmask)
print(kp)
img = cv2.drawKeypoints(foreg,kp,np.array([]),(0,0,255),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


im2,cont,heir = cv2.findContours(fmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


font = cv2.FONT_HERSHEY_SIMPLEX
for k in kp:
	img = cv2.putText(img,'blob',(int(k.pt[0]),int(k.pt[1])),font,1,(0,0,255),1,cv2.LINE_AA)

img = cv2.drawContours(img,cont,-1,(0,255,0),2)
cv2.imshow('blob',img)
cv2.waitKey(0)