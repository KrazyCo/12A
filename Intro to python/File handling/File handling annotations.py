def openFile(name,mode):
  try:
    name=name+".txt"            # Trys to open the file, if it fails (for example if there is not a file named this) it prints "Error: unable to open"
    myFile = open(name,mode)
    return myFile               # Returns the file refrence if it can be opened
  except:
    print("Error: unable to open", name)
    return False                # Returns False if there is no file to open

while True: # Main loop
  x = input("What would you like to do? ").upper() # User input and makes upper case
  if x == "ADD": # Checking if user input is add
    name = input("What is the name of the file you would like to open? ") # Asks user for the name of the file
    myFile = openFile(name,"a")   # calls openFile function with parameters name and "a" for append

    if myFile: # Checking if there was a file returned from the funtion
      item = input("What would you like to add? ") # Asks user for what they want to append to the document
      myFile.write(item) # Writes what the user inputted
      myFile.write("\n") # Writes empty line
      myFile.close()     # Closes the file
    print()              # prints empty line to console

  elif x == "SHOW": # Checking if user input is show
    name = input("What is the name of the file you would like to display? ") # Asks user for the name of the file
    myFile = openFile(name,"r") # calls openFile function with parameters name and "r" for read
    
    if myFile: # Checking if there was a file returned from the funtion
      linecnt = 1 # Linecount variable
      line = myFile.readline() # reads a single line from the file, and stores it as line
      while line!= "":         # While there is data in the line (condition loop)
        print("Line", linecnt, ":",line.strip()) # Prints the linecount and the contents of the line to the console
        line = myFile.readline() # reads the next line in the file
        linecnt = linecnt + 1 # adds 1 to the linecount

      if linecnt==1: # if there is no lines in the file
        print(name+".txt is empty")
      myFile.close() # close the file
      print() # prints empty line
      
  elif x == "NEW": # Checking if user input is new
    name = input("What is the name of your file? ") # asks user for the name of the file to create
    myFile = openFile(name,"w") # calls openFile function, opening the file in write mode, creating the file 
    myFile.close() # closes the file
    print() # prints empty line
    
  elif x=="STOP": # Checking if user input is stop
    break # breaks out of while true loop

print() # prints empty line
print("Thanks for coming - bye") # says bye