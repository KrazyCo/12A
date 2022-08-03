from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="bruh")
    myLabel.pack()

myButton = Button(root, text="click me", padx=10, pady=10, command=myClick, fg="blue", bg="red")

myButton.pack()

root.mainloop()