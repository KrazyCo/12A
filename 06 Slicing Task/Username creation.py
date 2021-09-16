firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

uname1 = firstName.lower() + lastName.upper()
print(uname1)

uname2 = firstName[0].upper() + lastName.upper()
print(uname2)

uname3 = firstName[0].lower() + lastName[0:3].lower()
print(uname3)

while True:
    uname = input("\nWhat username do you want to use? ")
    if len(uname) >= 4 and len(uname) <= 12:
        break
    else:
        print("Username not accepted, it must be at least 4 characters and no more than 12 characters")

if uname == uname1:
    print("You picked the first choice")
elif uname == uname2:
    print("You picked the second choice")
elif uname == uname3:
    print("You picked the third choice")
else:
    print("You choose your own username")