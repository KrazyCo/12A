from tkinter import *
from turtle import pos, position
from PIL import ImageTk,Image

root = Tk()

# pls ignore what the images are
myImg1 = ImageTk.PhotoImage(Image.open("images/nob.png").resize((500, 500), Image.ANTIALIAS))
myImg2 = ImageTk.PhotoImage(Image.open("images/oatmeal.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("images/joe being goofy.jpg").resize((396, 496), Image.ANTIALIAS))

imageList = [myImg1, myImg2, myImg3]
position = 0

myLabel = Label(image=imageList[position])
myLabel.grid(row=0, column=0, columnspan=3)

def forward():
    global position
    global myLabel
    global imageList
    global buttonBack
    global buttonForwards

    position+=1

    buttonBack = Button(root, text="<<", command=back)
    if position == len(imageList)-1:
        buttonForwards = Button(root, text=">>", command=forward, state=DISABLED)
    buttonBack.grid(row=1, column=0)
    buttonForwards.grid(row=1, column=2)

    myLabel.grid_forget()
    myLabel = Label(image=imageList[position])
    myLabel.grid(row=0, column=0, columnspan=3)

def back():
    global position
    global myLabel
    global imageList
    global buttonBack
    global buttonForwards

    position-=1

    buttonForwards = Button(root, text=">>", command=forward)
    if position == 0:
        buttonBack = Button(root, text="<<", command=back, state=DISABLED)
    buttonBack.grid(row=1, column=0)
    buttonForwards.grid(row=1, column=2)

    myLabel.grid_forget()
    myLabel = Label(image=imageList[position])
    myLabel.grid(row=0, column=0, columnspan=3)

buttonBack = Button(root, text="<<", command=back, state=DISABLED)
buttonQuit = Button(root, text="Exit", command=root.quit)
buttonForwards = Button(root, text=">>", command=forward)

buttonBack.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
buttonForwards.grid(row=1, column=2)

root.mainloop()