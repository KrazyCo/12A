from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0, "GIVE NAME")

def myClick():
    text = "Hello " + e.get()
    myLabel = Label(root, text=text)
    myLabel.pack()

myButton = Button(root, text="give name", command=myClick)

myButton.pack()

root.mainloop()