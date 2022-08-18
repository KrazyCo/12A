from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

root = Tk()

root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))

Label(root, text=root.filename).pack()

myImage = ImageTk.PhotoImage(Image.open(root.filename))
Label(root, image=myImage).pack()

root.mainloop()