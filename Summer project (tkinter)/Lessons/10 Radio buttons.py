from tkinter import *

root = Tk()

# r = IntVar()

def clicked(value):
    myLabel = Label(root, text=isit.get())
    myLabel.pack()

MODES = [
    "ahh",
    "eee",
    "woah",
    "cap"
]

isit = StringVar()
isit.set("ahh")

for i in MODES:
    Radiobutton(root, text=i, variable=isit, value=i, command=lambda: clicked(isit.get())).pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=isit.get())
myLabel.pack()

root.mainloop()