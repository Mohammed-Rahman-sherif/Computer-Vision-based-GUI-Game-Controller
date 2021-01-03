from tkinter import *
from tkinter import messagebox as msg 
import sqlite3

window = Tk()
window.title("FoToSo Play Console")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()

window.geometry('%dx%d+0+0' % (width,height))
p1 = PhotoImage(file = 'log.png')
window.iconphoto(False, p1)
#window.wm_attributes('-fullscreen','true') # -- FULL SCREEN

Name = StringVar()
Email = StringVar()
Password = StringVar()
Mobile = StringVar()

Name.set('')
Email.set('')
Password.set('')
Mobile.set('')

conn = sqlite3.connect('dbase.db')
cursor = conn.cursor()
cursor.execute('create table if not exists "usertable1" (Name text, Email text, Password int, Mobile int)')
conn.commit()

####################################################

def Next():
	conn = sqlite3.connect('dbase.db')
	cursor = conn.cursor()
	N = str(Name.get())
	#print(len(N(-5)))
	E = str(Email.get())
	#print(str(E)[-10:])
	e = str(E)[-10:]
	#print(len(E(-10)))
	P = str(Password.get())
	M = str(Mobile.get())
	m = len(M)
	if e == '@gmail.com' and m == 10:
		cursor.execute('insert into "usertable1" (Name, Email, Password, Mobile) values(?,?,?,?)', (N, E, P, M))
		msg.showinfo("confirmation message", 'User Account Created Successfully!', icon = 'info')
		conn.commit()
	else:
		msg.showinfo("Warning!", 'Plese Enter Valid Details!', icon = 'warning')

def back():
	window.destroy()
	import user_page
####################################################

#####################################################

img = PhotoImage(file = "hbg.png");
label = Label(window, image = img)
label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#####################################################

#####################################################

frame1 = Frame(window, width = 500)
frame1.grid(row = 0, column = 0, padx = 650, pady = 30)

label1 = Label(frame1, text = "Welcome Dear User!", font = ('Times New Roman', 25), fg = "red", bg = "silver")
label1.grid(row = 0, column = 0)


frame2 = Frame(window, width = 1000)
frame2.grid(row = 2, column = 0, padx = 650, pady = 100)

label3 = Label(frame2, text = "Name", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label3.grid(row = 1, column = 0, pady = 10)

tb3 = Entry(frame2, textvariable = Name, font = ('Times New Roman', 15))
tb3.grid(row = 1, column = 1, padx = 10, pady = 10)

label5 = Label(frame2, text = "E-mail", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label5.grid(row = 2, column = 0, pady = 10)

tb5 = Entry(frame2, textvariable = Email, font = ('Times New Roman', 15))
tb5.grid(row = 2, column = 1, padx = 10, pady = 10)

label6 = Label(frame2, text = "Password", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label6.grid(row = 3, column = 0, pady = 10)

tb6 = Entry(frame2, textvariable = Password, font = ('Times New Roman', 15))
tb6.grid(row = 3, column = 1, padx = 10, pady = 10)

label7 = Label(frame2, text = "Mobile", font = ('Times New Roman', 15), fg = "blue", bg = "white")
label7.grid(row = 4, column = 0, pady = 10)

tb7 = Entry(frame2, textvariable = Mobile, font = ('Times New Roman', 15))
tb7.grid(row = 4, column = 1, padx = 10, pady = 10)

btn1 = Button(frame2, text = 'Next', command = Next, bg = 'green', fg = 'white', font = ('Verdana', 15))
btn1.grid(row = 6, column = 0, ipadx = 10, ipady = 5, padx = 50, pady = 20)

btn2 = Button(frame2, text = 'Back', command = back, bg = 'black', fg = 'white', font = ('Verdana', 15))
btn2.grid(row = 6, column = 1, ipadx = 10, ipady = 5, padx = 50, pady = 20)

######################################################

window.mainloop()