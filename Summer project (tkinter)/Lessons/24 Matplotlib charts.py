from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry("400x200")

def graph():
    housePrices = np.random.normal(200000, 25000, 5000)
    plt.hist(housePrices, 200)
    plt.show()

Button(root, text="Graph it", command=graph).pack()


root.mainloop()