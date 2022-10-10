from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn To Code at datacamp.com')
root.iconbitmap('D:\Tkinter\pics\icon.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('My Second Window')
	top.iconbitmap('D:\Tkinter\pics\icon.ico')
	my_img = ImageTk.PhotoImage(Image.open("pics\dc.png"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Windo", command=open).pack()

mainloop()