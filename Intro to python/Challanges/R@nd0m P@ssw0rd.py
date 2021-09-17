import random
import string

letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

passwordLength = int(input("How long do you want your password to be? "))

print("Enter a 1 for yes, 0 for no")
if 