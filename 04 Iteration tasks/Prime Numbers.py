print("Prime Number Output\n")
userNumber = int(input("Enter the number to go up to: "))
#Task 1 - ask the user for a number

#Task 2 - complete the for loop below
for number in range(1,userNumber+1):
  #Task 3 - What condition should be entered after the or
  if number % number == 0 or number % 1 == 1:
    print(number)