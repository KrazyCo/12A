from tkinter import *
import sqlite3
from pathlib import Path

root = Tk()

# find current dir for file stuff
currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")

# Create database
db = sqlite3.connect(currDir+"/Databases/address_book.db")

# Create cursor
c = db.cursor()

# create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    phone_number interger
)""")

# commit and close
db.commit()
db.close()

# root.mainloop()