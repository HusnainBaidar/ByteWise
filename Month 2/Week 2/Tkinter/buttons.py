from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Button clicked completed!!")
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick,padx=70,pady=10,bg="Black",fg="White")
myButton.pack()



root.mainloop()