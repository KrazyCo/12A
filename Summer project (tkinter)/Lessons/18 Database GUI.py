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
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     phone_number interger
# )""")

# Submit function
def submit():
    # Create database
    db = sqlite3.connect(currDir+"/Databases/address_book.db")

    # Create cursor
    c = db.cursor()

    c.execute("INSERT INTO addresses VALUES (:fName, :lName, :address, :city, :pNumber)",
    {
        "fName": fName.get(),
        "lName": lName.get(),
        "address": address.get(),
        "city": city.get(),
        "pNumber": pNumber.get()
    })

    # commit and close
    db.commit()
    db.close()

    # Clear the textboxes
    fName.delete(0,END)
    lName.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    pNumber.delete(0,END)

# Create query function
def query():
    # Create database
    db = sqlite3.connect(currDir+"/Databases/address_book.db")

    # Create cursor
    c = db.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    printRecords = ""
    for record in records:
        printRecords += str(record) + "\n"

    queryLabel = Label(root, text=printRecords)
    queryLabel.grid(row=8, column=0, columnspan=2)

    # commit and close
    db.commit()
    db.close()

# Create labels and text entry
Label(root, text="First name").grid(row=0, column=0)
fName = Entry(root, width=30)
fName.grid(row=0, column=1, padx=20)

Label(root, text="Last name").grid(row=1, column=0)
lName = Entry(root, width=30)
lName.grid(row=1, column=1, padx=20)

Label(root, text="Address").grid(row=2, column=0)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

Label(root, text="City").grid(row=3, column=0)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

Label(root, text="Phone number").grid(row=4, column=0)
pNumber = Entry(root, width=30)
pNumber.grid(row=4, column=1, padx=20)

# Create submit button
submitBtn = Button(root, text="Add to Database", command=submit)
submitBtn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
queryBtn = Button(root, text="Show records", command=query)
queryBtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=108)

# commit and close
db.commit()
db.close()

root.mainloop()