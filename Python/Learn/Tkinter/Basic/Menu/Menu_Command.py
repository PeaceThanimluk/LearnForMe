from tkinter import *

root = Tk()
root.title("MyGui")
root.geometry("500x500")

#Create New Window Function
def showWindow():
    window = Tk()
    window.title("New Window")
    window.mainloop()

#Create Menu
myMenu = Menu()
root.config(menu=myMenu)

#Create Menu Item
MenuItem = Menu()
MenuItem.add_command(label="New Window", command=showWindow) #Use showWindow Function
MenuItem.add_command(label="New File")
MenuItem.add_command(label="Open File")
MenuItem.add_command(label="Save File")
MenuItem.add_command(label="About")
MenuItem.add_command(label="Exist")

#Add Menu
myMenu.add_cascade(label="File", menu=MenuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()