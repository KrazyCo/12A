import random
import string

chars = []
password = ""


passwordLength = int(input("How many characters do you want in your password? "))

print("Enter a 1 for yes, 0 for no")
if int(input("Do you want letters in your password? ")) == 1:
    for i in list(string.ascii_lowercase):
        chars.append(i)
    if int(input("Do you want capital letters in your password? ")) == 1:
        for i in list(string.ascii_uppercase):
            chars.append(i)
if int(input("Do you want numbers in your password? ")) == 1:
    for i in list(string.digits):
        chars.append(i)
if int(input("Do you want symbols in your password? ")) == 1:
    for i in list(string.punctuation):
        chars.append(i)

for i in range(passwordLength):
    password += str(chars[random.randint(0,len(chars)-1)])
    
print("Your password is:")
print(password)