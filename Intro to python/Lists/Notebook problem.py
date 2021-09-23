notes = ["Yo uh", "Hey guys today", "b", "Lets get political", "omg number four", "HELLO I AM A NOTE", "cant think of anything", "are we there yet", "bruh", "im going to rob someone"]

def showNotes():
    for i in range(len(notes)):
        print("%s: %s" % (i, notes[i]))

while True:
    showNotes()
    userInput = int(input("Enter the number of a note to change: "))
    userNoteInput = input("Enter the note to replace note %s: " % userInput)
    notes[userInput] = userNoteInput