from cProfile import label
from tkinter import *

root = Tk()

# for i in range(1000):
#     dumb = Toplevel()

def open():
    top = Toplevel() 
    Button(top, text="die", command=top.destroy).pack()

Button(root, text="Open second window", command=open).pack()

# top = Toplevel()

# Label(top, text="AHHHH").pack()

root.mainloop()