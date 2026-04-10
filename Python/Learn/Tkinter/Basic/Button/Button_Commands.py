from tkinter import *

#Create Gui
root = Tk()
root.title("MyGui")

#Set Gui Size
root.geometry("1920x1080")

#Create Text
mylabel = Label(root,text="HelloWorld",fg="red",font=20,bg="yellow").pack()

#Button Function
def showMessage():
    print("HellowWorld!")

#Create Button
Button1 = Button(
    root,
    text="Save",
    bg="lime",
    command=showMessage, #Use show_Message Function
).pack()

#Run
root.mainloop()

