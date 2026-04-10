from tkinter import *

#Create Gui
root = Tk()
root.title("MyGui")

#Set Gui Size
root.geometry("1920x1080")

#Create Text
mylabel = Label(root,text="HelloWorld",fg="red",font=20,bg="yellow").pack()

#Create Button
Button1 = Button(root, text="save").pack()

#Run
root.mainloop()

