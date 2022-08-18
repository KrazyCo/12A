from tkinter import *

root = Tk()

def dropdown(var):
    print(var)

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=dropdown).pack()

root.mainloop()