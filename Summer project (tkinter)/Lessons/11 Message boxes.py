from tkinter import *
from tkinter import messagebox

root = Tk()

def popup():
    response = messagebox.askyesno("This is my popup", "shut it shady")
    Label(root, text=response).pack()

Button(root, text="click me", command=popup).pack()

root.mainloop()