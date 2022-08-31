from tkinter import *
from tkinter import messagebox
import sqlite3
from pathlib import Path

root = Tk()
root.title("Account manager")
root.geometry("300x250")

def login():
    global logWin
    logWin = Toplevel()
    logWin.title("Login")
    logWin.geometry("300x250")

    titleText = Label(logWin, text="Login", width="33", bg="grey",  height="2", font=("Calibri", 13))
    titleText.grid(row=0, column=0, columnspan=2, pady=(0,10))
    Label(logWin, text="Username", height="2", width="10").grid(row=1, column=0)
    Label(logWin, text="Password", height="2", width="10").grid(row=2, column=0)

    global usernameEntryLog
    global passwordEntryLog

    usernameEntryLog = Entry(logWin).grid(row=1, column=1)
    passwordEntryLog = Entry(logWin).grid(row=2, column=1)

    loginButton = Button(logWin, text="Login", width="35", command=loginDB)
    loginButton.grid(row=5, column=0, columnspan=2, pady=10)

def loginDB():
    # Connect to DB
    currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")
    db = sqlite3.connect(currDir+"/accounts.db")
    c = db.cursor()

    c.execute("SELECT * FROM accounts WHERE username = " + usernameEntryLog.get())
    account = c.fetchone()

    print(account)

    # Close DB
    db.commit()
    db.close()

def register():
    global regWin
    regWin = Toplevel()
    regWin.title("Register")
    regWin.geometry("300x250")

    titleText = Label(regWin, text="Register", width="33", bg="grey",  height="2", font=("Calibri", 13))
    titleText.grid(row=0, column=0, columnspan=2, pady=(0,10))
    Label(regWin, text="Username", height="2", width="10").grid(row=1, column=0)
    Label(regWin, text="Password", height="2", width="10").grid(row=2, column=0)
    Label(regWin, text="First name", height="2", width="10").grid(row=3, column=0)
    Label(regWin, text="Last name", height="2", width="10").grid(row=4, column=0)

    global usernameEntryReg
    global passwordEntryReg
    global fnameEntryReg
    global lnameEntryReg

    usernameEntryReg = Entry(regWin)
    usernameEntryReg.grid(row=1, column=1)
    passwordEntryReg = Entry(regWin)
    passwordEntryReg.grid(row=2, column=1)
    fnameEntryReg = Entry(regWin)
    fnameEntryReg.grid(row=3, column=1)
    lnameEntryReg = Entry(regWin)
    lnameEntryReg.grid(row=4, column=1)

    loginButton = Button(regWin, text="Register", width="35", command=registerDB)
    loginButton.grid(row=5, column=0, columnspan=2, pady=10)

def registerDB():
    # Connect to DB
    currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")
    db = sqlite3.connect(currDir+"/accounts.db")
    c = db.cursor()

    print(usernameEntryReg.get())

    c.execute("SELECT * FROM accounts")
    accounts = c.fetchall()

    print(accounts)

    usernameTaken = False

    for account in accounts:
        if account[0] == usernameEntryReg.get():
            usernameTaken = True
            messagebox.showwarning(title="Register", message="That username is taken")
    
    if usernameTaken == False:
        c.execute("INSERT INTO accounts VALUES (:username, :password, :fname, :lname)",
            {
                "username": usernameEntryReg.get(),
                "password": passwordEntryReg.get(),
                "fname": fnameEntryReg.get(),
                "lname": lnameEntryReg.get()
            })

    regWin.destroy()

    # Close DB
    db.commit()
    db.close()

def show():
    global showWin
    showWin = Toplevel()
    showWin.title("Show accounts")
    showWin.geometry("300x250")

    # Connect to DB
    currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")
    db = sqlite3.connect(currDir+"/accounts.db")
    c = db.cursor()

    c.execute("SELECT * FROM accounts")
    global accounts
    accounts = c.fetchall()

    print(accounts)

    usernames = []

    for account in accounts:
        usernames.append(account[0])

    print(usernames)

    clicked = StringVar()
    clicked.set(usernames[0])

    drop = OptionMenu(showWin, clicked, *usernames, command=dropdown).grid(row=0, column=0, columnspan=2, pady=10)

    # Close DB
    db.commit()
    db.close()

def dropdown(var):
    print(var)
    Label(showWin, text="Username").grid(row=1, column=1)

Label(root, text="Account manager", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
Label(root, text="").pack()
Button(root, text="Login", height="2", width="30", command=login).pack()
Label(root, text="").pack()
Button(root, text="Register", height="2", width="30", command=register).pack()
Label(root, text="").pack()
Button(root, text="Show accounts", height="2", width="30", command=show).pack()

root.mainloop()
