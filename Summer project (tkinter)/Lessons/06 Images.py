from tkinter import *
from PIL import ImageTk,Image
from pathlib import Path

root = Tk()

# find current dir for file stuff
currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")

myImg = ImageTk.PhotoImage(Image.open(currDir+"/images/nob.png").resize((500, 500), Image.ANTIALIAS))
myLabel = Label(root, image=myImg)
myLabel.pack()

buttonQuit = Button(root, text="Exit", command=root.quit)
buttonQuit.pack()

root.mainloop()