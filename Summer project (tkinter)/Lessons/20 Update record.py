from tkinter import *
import sqlite3
from pathlib import Path

root = Tk()
root.title("Databases")

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

# Create function to delete record
def delete():
    # Create database
    db = sqlite3.connect(currDir+"/Databases/address_book.db")

    # Create cursor
    c = db.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid=" + deleteBox.get())

    # commit and close
    db.commit()
    db.close()

# Create edit function
def edit():
    global editor
    editor = Tk()
    editor.title("Edit a record")

    # Create database
    db = sqlite3.connect(currDir+"/Databases/address_book.db")

    # Create cursor
    c = db.cursor()

    # Query database
    record_id = deleteBox.get()
    c.execute("SELECT * FROM addresses WHERE oid =" + record_id)
    record = c.fetchone()

    

    # commit and close
    db.commit()
    db.close()

    # Create globals for text boxes
    global fNameEditor
    global lNameEditor
    global addressEditor
    global cityEditor
    global pNumberEditor

    # Create labels and text entry
    Label(editor, text="First name").grid(row=0, column=0)
    fNameEditor = Entry(editor, width=30)
    fNameEditor.grid(row=0, column=1, padx=20)

    Label(editor, text="Last name").grid(row=1, column=0)
    lNameEditor = Entry(editor, width=30)
    lNameEditor.grid(row=1, column=1, padx=20)

    Label(editor, text="Address").grid(row=2, column=0)
    addressEditor = Entry(editor, width=30)
    addressEditor.grid(row=2, column=1, padx=20)

    Label(editor, text="City").grid(row=3, column=0)
    cityEditor = Entry(editor, width=30)
    cityEditor.grid(row=3, column=1, padx=20)

    Label(editor, text="Phone number").grid(row=4, column=0)
    pNumberEditor = Entry(editor, width=30)
    pNumberEditor.grid(row=4, column=1, padx=20)

    # Create submit button
    submitBtnEditor = Button(editor, text="Update record", command=update)
    submitBtnEditor.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    fNameEditor.insert(0, record[0])
    lNameEditor.insert(0, record[1])
    addressEditor.insert(0, record[2])
    cityEditor.insert(0, record[3])
    pNumberEditor.insert(0, record[4])

# Update record
def update():
    # Create database
    db = sqlite3.connect(currDir+"/Databases/address_book.db")

    # Create cursor
    c = db.cursor()

    record_id = deleteBox.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        phone_number = :pNumber

        WHERE oid = :oid""",
        {
        "first": fNameEditor.get(),
        "last": lNameEditor.get(),
        "address": addressEditor.get(),
        "city": cityEditor.get(),
        "pNumber": pNumberEditor.get(),

        "oid": record_id
        })

    # commit and close
    db.commit()
    db.close()

    editor.destroy()

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
        printRecords += str(record[0]) + " " + str(record[1]) + " " + str(record[5]) + "\n"

    queryLabel = Label(root, text=printRecords)
    queryLabel.grid(row=10, column=0, columnspan=2)

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

# Create delete label
deleteLabel = Label(root, text="Select ID")
deleteLabel.grid(row=7, column=0, pady=(10,0))

# Create delete box
deleteBox = Entry(root, width=30)
deleteBox.grid(row=7, column=1, pady=(10,0))

# Create delete button
deleteBtn = Button(root, text="Delete record", command=delete)
deleteBtn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=108)

# Create an update button
updateBtn = Button(root, text="Edit record", command=edit)
updateBtn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=113)

# commit and close
db.commit()
db.close()

root.mainloop()