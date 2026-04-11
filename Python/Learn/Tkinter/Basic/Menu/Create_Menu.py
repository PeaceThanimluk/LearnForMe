from tkinter import *

root = Tk()
root.title("MyGui")
root.geometry("500x500")

#Create Menu
myMenu = Menu()
root.config(menu=myMenu)

#Add Menu
myMenu.add_cascade(label="Menu1")
myMenu.add_cascade(label="Menu2")
myMenu.add_cascade(label="Menu3")

root.mainloop()