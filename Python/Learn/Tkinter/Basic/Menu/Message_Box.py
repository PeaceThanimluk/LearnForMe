from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("MyGui")
root.geometry("500x500")

#Create New Window Function
def showWindow():
    window = Tk()
    window.title("New Window")
    window.mainloop()

def Show_Message_Box():
    tkinter.messagebox.showinfo("Title Info", "Baka")

#Create Menu
myMenu = Menu()
root.config(menu=myMenu)

#Create Menu Item
MenuItem = Menu()
MenuItem.add_command(label="New Window", command=showWindow) #Use showWindow Function
MenuItem.add_command(label="New File")
MenuItem.add_command(label="Open File")
MenuItem.add_command(label="Save File")
MenuItem.add_command(label="About", command=Show_Message_Box) #Use Show Message Box Function
MenuItem.add_command(label="Exist")

#Add Menu
myMenu.add_cascade(label="File", menu=MenuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()