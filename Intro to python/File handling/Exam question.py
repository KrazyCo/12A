datafile = "favourite.dat"

def showItems():
  pass


def addItem(barcode):
    f = open(datafile, "r")
    print(f.read())
  # open the file to read

  # read the first line

  # loop through the file till
  # a line has been read in and a match has not been found


        # check the barcode matched the line read in
  
        # if a match is found then record a match has been found

        # read the next line
        
  # close file when file read is finished
  
  # if no match is found then

    # open the file to append data

    # write the barcode to the file

    # close the file

# ================================
# MAIN CODE
# =================================
barcode = input("Enter the barcode: ")

addItem(barcode)