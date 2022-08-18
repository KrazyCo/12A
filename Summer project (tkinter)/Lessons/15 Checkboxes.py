from tkinter import *

root = Tk()

var = StringVar()

def ahh():
    print(var.get())

check = Checkbutton(root, text="AHHHHHH", variable=var, command=ahh, onvalue="ON", offvalue="OFF")
check.deselect() # fix for glitch
check.pack()



root.mainloop()