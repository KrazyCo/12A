from tkinter import *
from PIL import ImageTk,Image

root = Tk()

myImg = ImageTk.PhotoImage(Image.open("images/nob.png").resize((500, 500), Image.ANTIALIAS))
myLabel = Label(root, image=myImg)
myLabel.pack()

buttonQuit = Button(root, text="Exit", command=root.quit)
buttonQuit.pack()

root.mainloop()