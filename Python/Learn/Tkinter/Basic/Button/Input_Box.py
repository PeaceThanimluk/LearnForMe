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
    Message = Txt.get() #ดึงข้อความจากกล่องข้อความ
    print(Message)

#Input_Box(Entry)
Txt = StringVar() #เก็บข้อความ
My_Text = Entry(
    root,
textvariable=Txt
)
My_Text.pack()

#Create Button
Button1 = Button(
    root,
    text="Save",
    bg="lime",
    command=showMessage, #Use show_Message Function
)
Button1.pack()

#Run
root.mainloop()
