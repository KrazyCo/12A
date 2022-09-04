from tkinter import *
import datetime 

root = Tk()
root.title("Age calculator")
root.geometry("300x250")

def calculate():
    birthdate = datetime.date(int(year.get()), int(month.get()), int(day.get()))
    today = datetime.date.today()
    years = today.year - birthdate.year

    # remove 1 year if birthday has not passed in the year yet
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        years -= 1
    Label(root, text=f"You are {years} years old!").grid(row=4, column=0, columnspan=2, pady=10)

Label(root, text="Year").grid(row=0, column=0, pady=5, padx=10)
Label(root, text="Month").grid(row=1, column=0, pady=5, padx=10)
Label(root, text="Day").grid(row=2, column=0, pady=5, padx=10)

year = Entry(root)
year.grid(row=0, column=1, pady=5, padx=10)
month = Entry(root)
month.grid(row=1, column=1, pady=5, padx=10)
day = Entry(root)
day.grid(row=2, column=1, pady=5, padx=10)

Button(root, text="How old am I?", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()