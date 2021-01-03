import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Canvas, Frame, BOTH
from tkinter import messagebox as msg 
from pynput.keyboard import Key,Controller
import numpy as np
import time
import cv2

keyboard = Controller()

window = Tk()
p1 = PhotoImage(file = 'log.png')
window.iconphoto(False, p1)
window.title('Home')

width, height = window.winfo_screenwidth(), window.winfo_screenheight()

window.geometry('%dx%d+0+0' % (width,height))
#window.resizable(False, False)

##############################################################

def start():
	msg.showinfo("Guide Line", 'Dear user, Please wait for few minutes.. Now your Browser will open, then you will be redirected to a page, there subway suffers will be downloaded, wait there and after those installation process.. come back to FoToSo Play Console and press the activate.. this will activate your camera then only Facial Navigation will start working!!.. Thank you!', icon = 'info')
	import webbrowser
	webbrowser.open_new_tab('https://www.kiloo.com/subway-surfers/')  # Go to example.com

def activate():
	msg.askyesno(title = "Note", message = 'Hey buddy, Does subway suffers downloaded in your browser?', icon = 'question')
	msg.showinfo(title = "Warning", message = 'If you activate without entering into game screen, your PC may misbehave', icon = 'warning')

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

##############################################################

img = PhotoImage(file = "1.png");
label = Label(window, image = img)
label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

##############################################################

label1 = Label(window, text = ' Select Game :', font = ('Times New Roman', 25), fg = 'blue', bg = 'silver')
label1.place(x=400, y=200, anchor=NW)

##############################################################

'''style = ttk.Style()

style.map('TCombobox', fieldbackground=[('readonly','white')])
style.map('TCombobox', selectbackground=[('readonly', 'white')])
style.map('TCombobox', selectforeground=[('readonly', 'black')])

mycombo = ttk.Combobox(window, height=15,justify='left',width=21)

window.mycombo['state'] = 'readonly' # Set the state according to configure colors
window.mycombo.bind('<<ComboboxSelected>>',
                      lambda event: window._click_combo())
'''
##############################################################

ttk.Style().configure('TCombobox', relief='flat')
cmb = ttk.Combobox(window, state="readonly", width=20, font="Verdana 16 bold")
cmb['values'] = ('Subway Suffers','No More Games Available!')
cmb.current(0)
cmb.place(x=600, y=300, anchor=NW)

'''style = ttk.Style()
self.mycombo = ttk.Combobox(self.frame,textvariable=self.combo_var, height=15,justify='left',width=21, values=lista)
self.mycombo['state'] = 'readonly' # Set the state according to configure colors
self.mycombo.bind('<<ComboboxSelected>>', lambda event: self._click_combo())'''

frame1 = Frame(window, width = 300, bg = 'white')
frame1.place(x=400, y=400, anchor=NW)

img1 = PhotoImage(file = "s1.png");
label2 = Label(frame1, image = img1)
label2.grid(row = 0, column = 0)

btn1 = Button(window, text = 'Start', command = start, bg = 'green', width=8, font="Verdana 16 bold", fg = 'white')
btn1.place(x=400, y=600, anchor=NW)

btn2 = Button(window, text = 'Activate', command = activate, bg = 'blue', width=8, font="Verdana 16 bold", fg = 'white')
btn2.place(x=580, y=600, anchor=NW)

'''canvas = Canvas(window,bg = "green")
canvas.create_line(300, 35, 300, 200, dash=(4, 2))
canvas.place(x=800, y=600, anchor=NW)'''

frame2 = Frame(window, width = 300, bg = 'white')
frame2.place(x=850, y=400, anchor=NW)

img2 = PhotoImage(file = "g2p.png");
label3 = Label(frame2, image = img2)
label3.grid(row = 0, column = 0)

label4 = Label(window, text = ' Coming Soon!!!...', font = ('Times New Roman', 20), fg = 'purple', bg = 'yellow')
label4.place(x=850, y=600, anchor=NW)
window.mainloop()