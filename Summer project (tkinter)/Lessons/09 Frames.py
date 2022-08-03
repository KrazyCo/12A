from tkinter import *

root = Tk()

frame = LabelFrame(root, text="this is a frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

myButton = Button(frame, text="AHHHHH")
myButton.pack()

root.mainloop()