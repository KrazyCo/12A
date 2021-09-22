#Task 1: create a list called students where each index is the first name of a student in your class (minimum 5 students)

print('''
#######################
Year 10 Class List Menu
#######################

Type:
 - ADD to add a new student
 - SHOW to output the current class list
 - UPDATE to update an existing student
 - REMOVE to remove a student from the class list
 - EXIT to end the program
''')

students = ["Darin Greg", "Amelia Anaya", "Brand Diggory", "Jervis Leith", "Layla Nickolas"]

while True:
    menuChoice = input("What would you like to do? ")
    if menuChoice.upper() == "ADD":
        newStudent = input("What is the name of the new student? ")
        students.append(newStudent)
    elif menuChoice.upper() == "SHOW":
        print("There is %s students in the class:" % len(students))
        for i in range(len(students)):
            print("%s: %s" % (i+1, students[i]))
    elif menuChoice.upper() == "UPDATE":
        replaced = input("What is the name of the student to replace or the index of the student: ")
        if replaced.isnumeric():
            replacedStudent = students[int(replaced)-1]
            toReplace = input("What is the name of the student to replace %s: " % replacedStudent)
            students[int(replaced)-1] = toReplace
            print("Replaced %s with %s" % (replacedStudent, toReplace))
        else:
            toReplace = input("What is the name of the student to replace %s: " % replaced)
            replacedStudent = replaced
            students[students.index(replaced)] = toReplace
            print("Replaced %s with %s" % (replaced, toReplace))
    elif menuChoice.upper() == "REMOVE":
        removed = input("What is the name of the student to replace or the index? ")
        if removed.isnumeric():
            removedStudent = students[int(removed)-1]
            students.pop(int(removed)-1)
        else:
            removedStudent = removed
            students.remove(removed)
        print("Removed %s from the list" % removedStudent)
    elif menuChoice.upper() == "EXIT":
        print("Exiting...")
        break
    else:
        print("That is not a valid option, please type: ADD, SHOW, UPDATE, REMOVE or EXIT")