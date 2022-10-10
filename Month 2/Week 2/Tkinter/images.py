from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at datacamp.com')
root.iconbitmap('D:\Tkinter\pics\icon.ico')


my_img = ImageTk.PhotoImage(Image.open("pics\dc.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()