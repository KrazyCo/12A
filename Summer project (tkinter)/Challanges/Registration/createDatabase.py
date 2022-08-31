from tkinter import *
import sqlite3
from pathlib import Path

# find current dir for file stuff
currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")

# Create database
db = sqlite3.connect(currDir+"/accounts.db")

# Create cursor
c = db.cursor()

# create table
c.execute("""CREATE TABLE accounts (
    username text,
    password text,
    firstName text,
    lastName text
)""")

# commit and close
db.commit()
db.close()

