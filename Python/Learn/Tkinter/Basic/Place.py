from tkinter import *

#Create Gui
root = Tk()
root.title("MyGui")

#Set Gui Size
root.geometry("1920x1080")

#Create Text
mylabel = Label(root,text="HelloWorld",fg="red",font=20,bg="yellow").pack()

#Place Text
Place1 = Label(root,text="(0,0)",fg="red",font=20,bg="yellow").place(x=0,y=0)
Place2 = Label(root,text="(100,0)",fg="red",font=20,bg="yellow").place(x=100,y=0)
Place3 = Label(root,text="(100,300)",fg="red",font=20,bg="yellow").place(x=100,y=300)

#Grid Text
Grid = Label(root,text="(0,0)",fg="red",font=20,bg="yellow").grid(row=10,column=10)

#Run
root.mainloop()

