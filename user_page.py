from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

def login():
	window.destroy()
	import login

def create():
	window.destroy()
	import reg

window = Tk()
window.title('User Page')
p1 = PhotoImage(file = 'log.png')
window.iconphoto(False, p1)
window.geometry('512x427')
window.resizable(False, False)

		#############################################################

img = PhotoImage(file = "t3.png");
label = Label(window, image = img)
label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

		##############################################################

label1 = Label(window, text = 'Select Sign-In Option!', font = ('Times New Roman', 25), background = "white", foreground = 'dark green')
label1.grid(row = 0,column = 1, padx = 110, pady = 10)

'''label2 = Label(window, text = '                                ', font = ('Times New Roman', 15))
label2.grid(row = 0,column = 0)'''

'''label3 = Label(window, text = ' ', font = ('Times New Roman', 15))
label3.grid(row = 1,column = 0, padx = )
'''
'''label4 = Label(window, text = ' ', font = ('Times New Roman', 15))
label4.grid(row = 2,column = 0)

label5 = Label(window, text = ' ', font = ('Times New Roman', 15))
label5.grid(row = 3,column = 0)

label6 = Label(window, text = ' ', font = ('Times New Roman', 15))
label6.grid(row = 4,column = 0)'''

frame1 = Frame(window, width = 300)
frame1.grid(row = 5, column = 1, padx = 110, pady = 100)

'''label7 = Label(frame1, text = 'login', font = ('Times New Roman', 15), fg = 'green')
label7.grid(row = 0,column = 1)'''

#############################################################

style = ttk.Style() 
style.configure('TButton', font=('calibri', 15, 'bold', 'underline'),
foreground='red', background = 'blue')
#style.configure('W.TButton', font= ('Arial', 10, 'bold'), borderwidth = '4', foreground='Green')

btn1 = Button(frame1, text = 'Login!', command = login, style='TButton')
btn1.grid(row = 0, column = 2, padx = 50, pady = 10)

btn2 = Button(frame1, text = 'Create New Account', command = create, style='TButton')
btn2.grid(row = 1, column = 2, padx = 50, pady = 10)

#############################################################

'''label1 = Label(frame1, text = ' ', font = ('Times New Roman', 15), fg = 'green')
label1.grid(row = 0,column = 0)'''

window.mainloop()