print('''
===== MENU =====

1. Add name
2. Edit name
3. Remove name
''')

choice = int(input("enter your choice - "))
print()
print("You entered : " + str(choice))
print()

if choice == 1:
    print("the code will add a name")
elif choice == 2:
    print("the code will edit a name")
elif choice == 3:
    print("the code will remove a name")
else:
    print("invalid menu choice entered")
print("Finished")