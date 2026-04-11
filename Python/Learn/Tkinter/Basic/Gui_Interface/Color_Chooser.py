from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.title("My Gui")
root.geometry("500x500")

def Select_Color():
    color = askcolor()
    mylabel = Label(text="Hello" ,bg=color[1])
    mylabel.pack()

button = Button(text="Choose color" ,command=Select_Color)
button.pack()

root.mainloop()