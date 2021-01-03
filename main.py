from pynput.keyboard import Key,Controller
import numpy as np
import time
import cv2

keyboard = Controller()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
#	cv2.rectangle(img,(250, 180),(400,350),(255,0,0),5)
	cv2.rectangle(img,(240,170),(400,330),(255,0,255),3)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.1, 10)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1)
		center = (x+w/2, y+h/2)
		cv2.circle(img,(int(x+w/2), int(y+h/2)),(5),(0,0,255),-1)
		#print(z)

		if center <= (214, 480):
        #   print("left")
			fnt = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img,("LEFT:"),(0,40),fnt,1,(0,0,255),2)
			keyboard.release(Key.right)
			keyboard.release(Key.down)
			keyboard.release(Key.up)
			keyboard.press(Key.left)
		elif center[0] > (428):
        #   print('right')
			fnt = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img,("RIGHT:"),(428,40),fnt,1,(0,0,255),2)
			keyboard.release(Key.left)
			keyboard.release(Key.down)
			keyboard.release(Key.up)
			keyboard.press(Key.right)
		elif center[1] < (170) :
        #   print("center")
			fnt = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img,("UP:"),(215,40),fnt,1,(0,0,255),2)
			keyboard.release(Key.left)
			keyboard.release(Key.down)
			keyboard.release(Key.right)
			keyboard.press(Key.up)         
		elif center[1] > (330):
        #   print("center")
			fnt = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img,("DOWN:"),(215,40),fnt,1,(0,0,255),2)
			keyboard.release(Key.left)
			keyboard.release(Key.right)
			keyboard.release(Key.up)
			keyboard.press(Key.down)   
#		print(center)
	cv2.imshow('img', img)

	if cv2.waitKey(1) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
