#extract and find measurement
import cv2
import numpy as np
import time
import math
import sympy
#load images

show_images = True


def nop(x):
	pass

img_ref_rgb = cv2.imread('ref.jpg')
img_pos_rgb = cv2.imread('pos.jpg')
foregBGR = cv2.resize(img_pos_rgb,(480,360))
backgBGR = cv2.resize(img_ref_rgb,(480,360))

foreg = cv2.cvtColor(foregBGR,cv2.COLOR_BGR2HSV)
fore = cv2.cvtColor(foreg,cv2.COLOR_HSV2BGR)
backg = cv2.cvtColor(backgBGR,cv2.COLOR_BGR2HSV)
diff = cv2.absdiff(backg,foreg)

thresh = 10
ret,fmask = cv2.threshold(diff,thresh,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)
fmask = cv2.erode(fmask,kernel,iterations = 1)
fmask = cv2.dilate(fmask,kernel,iterations = 2)


res = cv2.cvtColor(cv2.bitwise_and(foreg,fmask),cv2.COLOR_HSV2BGR)




#blob some data
params = cv2.SimpleBlobDetector_Params()
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = False

detector = cv2.SimpleBlobDetector_create(params)

ffmask = cv2.cvtColor(fmask,cv2.COLOR_BGR2GRAY)


kp = detector.detect(fmask)
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
	if dist < bestdist:
		bestdist = dist
		best = i

print('best',i,int(bestdist))
#select the best contor

rect = cv2.boundingRect(contours[best])
#padding = 30
#rect[0] -= padding
#rect[1] -= padding
#rect[2] += padding
#rect[3] += padding
#rect = tuple(rect)
cv2.rectangle(img,rect[0:2],(rect[0]+rect[2],rect[1]+rect[3]),(255,0,0),1)

cv2.drawContours(img,contours,best,(255,0,0),2)

if show_images:
	cv2.imshow('diff',diff)
	cv2.imwrite('p_diff.jpg',diff)
	cv2.imshow('denoised',cv2.fastNlMeansDenoising(diff,None,10,5,5))
	cv2.imshow('foreground',fore)
	cv2.imshow('result',res)
	cv2.imwrite('p_res.jpg',res)
	cv2.imshow('blob, contours and rect',img)
	cv2.imwrite('p_blob.jpg',img)


#now try to measure the person.
#imagesize = 480,360
cx,cy = 240,180

deg = math.degrees(math.atan2(ky-cy,kx - cx))+90 #plus 90 for final rot

x,y,w,h = rect
pers = foregBGR[y:y+h,x:x+w]
persbg  = backgBGR[y:y+h,x:x+w]
rows,cols = h,w
#get average colour
avgr = np.average(pers,axis=0)
avgc = np.round(np.average(avgr,axis=0))
avgc = (255,255,255)

M = cv2.getRotationMatrix2D((cols/2,rows/2),deg,0.7)
pers = cv2.warpAffine(pers,M,(cols,rows),borderMode=cv2.BORDER_CONSTANT,borderValue=avgc)
persbg = cv2.warpAffine(persbg,M,(cols,rows),borderMode=cv2.BORDER_CONSTANT,borderValue=avgc)
pers = cv2.resize(pers,(480,360))
persbg = cv2.resize(persbg,(480,360))

cv2.imshow('person',pers)
cv2.imshow('persbg',persbg)


#height extraction


pers_g = cv2.cvtColor(pers,cv2.COLOR_BGR2GRAY)
norm = np.zeros(pers.shape)
normfg = cv2.normalize(pers,norm,0,255,cv2.NORM_MINMAX)
normbg = cv2.normalize(persbg,norm,0,255,cv2.NORM_MINMAX)

cv2.imshow('norm fg',normfg)
cv2.imshow('norm bg',normbg)
cv2.imwrite('p_normfg.jpg',normfg)
cv2.imwrite('p_normbg.jpg',normbg)

res = cv2.absdiff(normbg,normfg)
res = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
thresh = 20
ret,dmask = cv2.threshold(res,thresh,255,cv2.THRESH_BINARY)
dmask = cv2.dilate(dmask,kernel,iterations = 2)

cv2.imshow('difference image gry',res)
#cv2.imwrite('diff.jpg',res)

res = cv2.bitwise_and(cv2.cvtColor(normfg,cv2.COLOR_BGR2GRAY),dmask)
cv2.imshow('difference subtracted',res)
cv2.imwrite('p_normdiff.jpg',res)

thg = cv2.adaptiveThreshold(res,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
thm = cv2.adaptiveThreshold(res,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

kernel = np.ones((3,3),np.uint8)

thm = cv2.erode(thm,kernel,iterations = 3)
thg = cv2.erode(thg,kernel,iterations = 1)
#thm = cv2.dilate(thm,kernel,iterations = 1)

threshimg = thm
#threshimg = np.zeros((720,480))
#threshimg[0:360,0:480] = thg[:,:]
#threshimg[360:,0:480] = thm[:,:]

im2, cont, hierarchy = cv2.findContours(threshimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(cont))
res = cv2.drawContours(normfg,cont,-1,(0,0,255),1)
x,y,w,h = cv2.boundingRect(cont[0])

for e in cont:
	xx,yy,ww,hh = cv2.boundingRect(e)
	tl = min(x,xx),min(y,yy)
	br = max(x+w,xx+ww),max(y+h,yy+hh)
	

res = cv2.rectangle(res,tl,br,(255,0,0),1)

pix_height = abs(tl[1] - br[1])
real_height = 160
pix_m = pix_height / real_height
s = "pix {}".format(pix_height)
s1 = "known/est height {}cm".format(real_height)
s2 = "pixel per cm: {:02}".format(pix_m)

res = cv2.putText(res,s,(0,20),font,0.5,(255,0,255),1,cv2.LINE_AA)
res = cv2.putText(res,s1,(0,40),font,0.5,(255,0,255),1,cv2.LINE_AA)

cv2.imshow('thresh comparison',res)
cv2.imwrite('p_ds.jpg',res)


#get some real testing going on









cv2.waitKey(0)