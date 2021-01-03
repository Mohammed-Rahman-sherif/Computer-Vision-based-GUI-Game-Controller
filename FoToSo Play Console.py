import cv2
from tkinter import *
from tkinter import ttk
import numpy as np

cap = cv2.VideoCapture('wing2_mod.mp4')

if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

##############################################################

window = Tk()
p1 = PhotoImage(file = 'log.png')
window.iconphoto(False, p1)
window.title('FoToSo Play Console')
#window.iconbitmap('logo1.jpg')
#window.wm_attributes('-fullscreen','true') # -- FULL SCREEN
#window.eval('tk::PlaceWindow . center') # -- CENTER SCREEN
#window.overrideredirect(1) # -- TITLE BAR LESS SCREEN

width, height = window.winfo_screenwidth(), window.winfo_screenheight()

window.geometry('%dx%d+0+0' % (width,height))
window.resizable(False, False)

##############################################################

img = PhotoImage(file = "dots.png");
label = Label(window, image = img)
label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

##############################################################

style = ttk.Style()
style.theme_use('clam')

style.configure("Vertical.TScrollbar", gripcount=0,
background="gold", darkcolor="DarkGreen", lightcolor="LightGreen",
troughcolor="black", bordercolor="blue", arrowcolor="white")

def check_checkbox () :
  if chk.get () == 1:
    btn1['state'] = 'normal'
  else:
    btn1['state'] = 'disabled'

def cancel():
	window.destroy()

def Next():
  window.destroy()
  import user_page

wrapper1 = Label(window)
wrapper2 = Label(window, bg = 'black')

im = PhotoImage(file = "dots.png");
labe = Label(wrapper2, image = im)
labe.place(x = 0, y = 0, relwidth = 1, relheight = 1)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side = LEFT, fill = 'both', expand = 'yes')

yscrollbar = ttk.Scrollbar(wrapper1, orient = 'vertical', command = mycanvas.yview)
yscrollbar.place(x=5, y=5, width=150)
yscrollbar.set(0.2,0.3)
yscrollbar.pack(side = RIGHT, fill = 'y')

mycanvas.configure(yscrollcommand = yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window = myframe, anchor = 'nw')

label1 = Label(myframe, text = '            Welcome Dear Gamer!            ', font = ('Times New Roman', 25), fg = 'green')
label1.pack()
label26 = Label(myframe, text = ' ', font = ('Arial', 10), fg = 'blue')
label26.pack()
label2 = Label(myframe, text = 'By marking tick in the checkbox, we assume that your accepting                ', font = ('Arial', 10), fg = 'blue')
label2.pack()
label3 = Label(myframe, text = 'our terms and conditions. Do not continue to use our FoToSo Play               ', font = ('Arial', 10), fg = 'blue')
label3.pack()
label4 = Label(myframe, text = 'Console if you do not agree to take all of the terms and conditions               ', font = ('Arial', 10), fg = 'blue')
label4.pack()
label8 = Label(myframe, text = 'stated below. ', font = ('Arial', 10), fg = 'blue')
label8.pack()
label10 = Label(myframe, text = ' ', font = ('Arial', 10), fg = 'blue')
label10.pack()
label9 = Label(myframe, text = '  LICENSE :                                                                               ', font = ('Times New Roman', 15), fg = 'green')
label9.pack()
label5 = Label(myframe, text = 'Unless otherwise stated, Video Game Controller and/or its licensors             ', font = ('Arial', 10), fg = 'black')
label5.pack()
label6 = Label(myframe, text = 'own the  intellectual property rights for all material on Video Game              ', font = ('Arial', 10), fg = 'black')
label6.pack()
label7 = Label(myframe, text = 'Controller. All for your own personal use subjected to restrictions set              ', font = ('Arial', 10), fg = 'black')
label7.pack()
label11 = Label(myframe, text = 'in these terms and conditions. ', font = ('Arial', 10), fg = 'black')
label11.pack()
label12 = Label(myframe, text = ' ', font = ('Arial', 10), fg = 'black')
label12.pack()
label13 = Label(myframe, text = ' You Must Not :                                                                          ', font = ('Times New Roman', 15), fg = 'green')
label13.pack()
label14 = Label(myframe, text = '          ➡ Republish material from Video Game Controller                                            ', font = ('Arial', 10), fg = 'black')
label14.pack()
label15 = Label(myframe, text = '          ➡ Sell, rent or sub-license material from Video Game Controller                        ', font = ('Arial', 10), fg = 'black')
label15.pack()
label16 = Label(myframe, text = '      ➡ Reproduce, duplicate or copy material from Video Game Controller            ', font = ('Arial', 10), fg = 'black')
label16.pack()
label20 = Label(myframe, text = '          ➡ Redistribute content from Video Game Controller                                         ', font = ('Arial', 10), fg = 'black')
label20.pack()
label18 = Label(myframe, text = ' ', font = ('Arial', 10), fg = 'blue')
label18.pack()
label17 = Label(myframe, text = ' Disclaimer :                                                                               ', font = ('Times New Roman', 15), fg = 'green')
label17.pack()
label19 = Label(myframe, text = 'we will not be liable for any loss or damage of any nature.', font = ('Arial', 10), fg = 'black')
label19.pack()
label22 = Label(myframe, text = ' ', font = ('Arial', 10), fg = 'blue')
label22.pack()
label21 = Label(myframe, text = ' Note :                                                                                        ', font = ('Times New Roman', 15), fg = 'green')
label21.pack()
label23 = Label(myframe, text = 'USE OUR CONSOLE ONLY IF U HAVE A GPU AND GOOD  ', font = ('Arial', 10), fg = 'red')
label23.pack()
label24 = Label(myframe, text = 'VERSION OF PROCESSOR IN YOUR PC / LAPTOP  ', font = ('Arial', 10), fg = 'red')
label24.pack()
label25 = Label(myframe, text = 'Thank You !!!...', font = ('Arial', 10), fg = 'black')
label25.pack()

#####################
#####################

wrapper1.pack(fill = 'both', expand = 'yes', padx = 500, pady = 100)
wrapper2.pack(fill = 'both', expand = 'yes', padx = 500, pady = 10)

#ttk.Separator(wrapper2).place(x=0, y=28, relwidth=1)

chk = BooleanVar();

tick = Checkbutton(wrapper2, text = 'Accept Privacy Policy', font = 'Helvetica 11 bold', bg = "silver", fg = 'blue', command = check_checkbox, variable = chk, onvalue = 1, offvalue = 0)
tick.grid(row = 5, column = 0, padx = 180)
#tick.pack(side = TOP, fill = 'y')

'''lab1 = Label(wrapper2, text = ' ', font = ('Arial', 10))
#lab1.grid(row = 6, column = 0)
lab1.pack()'''

'''lab2 = Label(wrapper2, text = ' ', font = ('Arial', 10))
#lab2.grid(row = 7, column = 0)
lab2.pack()'''

frame1 = Frame(wrapper2, width = 500, bg = 'black')
frame1.grid(row = 8, column = 0, padx = 10, pady = 50)
#frame1.pack()

'''lab3 = Label(frame1, text = '                        ', font = ('Arial', 10), fg = 'black')
lab3.pack()'''
#lab3.grid(row = 1, column = 0)

btn1 = Button(frame1, text = 'Next', command = Next, bg = 'green', fg = 'white', font = 'Helvetica 11 bold')
btn1['state'] = 'disabled'
#btn1.pack(side = LEFT, fill = 'x')
btn1.grid(row = 1, column = 1, padx = 50, pady = 10)

btn2 = Button(frame1, text = 'Cancel', command = cancel, bg = 'red', fg = 'white', font = 'Helvetica 11 bold')
btn2.grid(row = 1, column = 2, padx = 50, pady = 10)
#btn2.pack(side = RIGHT, fill = 'x')

'''lab4 = Label(frame1, text = '                        ', font = ('Arial', 10), fg = 'black')
lab4.grid(row = 1, column = 3)'''
#lab4.pack()

window.mainloop()