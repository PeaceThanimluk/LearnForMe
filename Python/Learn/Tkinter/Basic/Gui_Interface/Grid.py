from tkinter import *

#Create Gui
root = Tk()
root.title("MyGui")

#Set Gui Size
root.geometry("1920x1080")

#Create Grid
mylabel = Label(root,text="HelloWorld",fg="red",font=20,bg="yellow").grid(row=0,column=0)

#Run
root.mainloop()

