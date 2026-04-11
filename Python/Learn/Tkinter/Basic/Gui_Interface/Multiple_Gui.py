from tkinter import *

#Create Gui
root = Tk()
root.title("MyGui")

#Set Gui Size
root.geometry("1920x1080")

#Button Function
def showMessage():
    Message = Txt.get() #ดึงข้อความจากกล่องข้อความ
    print(Message)

def openWindow():
    #Create Second Gui
    Second_Gui = Tk()
    Second_Gui.title("Second Gui")
    Second_Gui.geometry("500x300")

#Create Text
mylabel = Label(root,text="HelloWorld",fg="red",font=20,bg="yellow").pack()

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

#Open Window Button
Open_Window_Button = Button(
    root,
    text="Open Window",
    command=openWindow
)
Open_Window_Button.pack()

#Run
root.mainloop()
