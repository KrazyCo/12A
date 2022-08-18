from tkinter import *

root = Tk()
root.geometry("400x400")

def update(value):
    # myStringVar.set(horizontal.get())
    myStringVar.set(value)


verticle = Scale(root, from_=0, to=100)
verticle.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=update)
horizontal.pack()

myStringVar = StringVar()
myStringVar.set("0")
myLabel = Label(root, textvariable=myStringVar).pack()

Button(root, text="click me", command=update).pack()


root.mainloop()