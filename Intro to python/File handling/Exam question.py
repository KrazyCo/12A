datafile = "favourite.dat"

def showItems():
  pass


def addItem(barcode):
    f = open(datafile, "r")         # open the file in read mode
    found = False
    print(f"{f.readlines()=}")
    print(f"{barcode in f.readlines()=}")
    print(f"{len(f.readlines())=}")
    for i in range(len(f.readlines())):
        print(f.readline())

    # if not found:                   # if the barcode isnt already in the file
    #     f = open(datafile, "a")     # open the file in append mode
    #     f.write(f"\n{barcode}")     # append the barcode with a new line at the start
    #     f.close()                   # close the file

# ================================
# MAIN CODE
# =================================
barcode = input("Enter the barcode: ")

addItem(barcode)