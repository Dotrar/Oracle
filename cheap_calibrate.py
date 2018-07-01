import cv2


print('calibrate cameras')

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