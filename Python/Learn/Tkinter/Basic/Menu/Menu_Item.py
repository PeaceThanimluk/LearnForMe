from tkinter import *

root = Tk()
root.title("MyGui")
root.geometry("500x500")

#Create Menu
myMenu = Menu()
root.config(menu=myMenu)

#Create Menu Item
MenuItem = Menu()
MenuItem.add_command(label="New File")
MenuItem.add_command(label="Open File")
MenuItem.add_command(label="Save File")
MenuItem.add_command(label="About")
MenuItem.add_command(label="Exist")

#Add Menu
myMenu.add_cascade(label="Menu1", menu=MenuItem)
myMenu.add_cascade(label="Menu2")
myMenu.add_cascade(label="Menu3")

root.mainloop()