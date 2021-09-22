import string

weak = ["password" , "qwerty" , "hello123" , "letmein" , "123456"]

def securePassword(password):
    for weakPassword in weak:
        if password == weakPassword:
            return False
    if len(password) <= 8:
        return False
    lowercaseLetter = False
    uppercaseLetter = False
    specialChar = False
    for i in string.ascii_lowercase:
        if i in password:
            lowercaseLetter = True
    for i in string.ascii_uppercase:
        if i in password:
            uppercaseLetter = True
    for i in string.punctuation:
        if i in password:
            specialChar = True
    if lowercaseLetter and uppercaseLetter and specialChar:
        return True
    else:
        return False

userPassword = input("Give me your password: ")
if securePassword(userPassword):
    print("Password accepted")
else:
    while True:
        userPassword = input("Password too weak, enter a diffrent password: ")
        if securePassword(userPassword):
            print("Password accepted")
            break