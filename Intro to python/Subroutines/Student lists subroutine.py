class Students:
    studentList = ["Darin Greg", "Amelia Anaya", "Brand Diggory", "Jervis Leith", "Layla Nickolas"]

    def addStudent(self, student):
        self.studentList.append(student)
        print(f"Added {student} to the list")

    def getStudents(self):
        return self.studentList

    def updateStudent(self, toReplace, replaceWith):
        if toReplace.isnumeric():
            try:
                repalacedStudent = self.studentList[int(toReplace)-1]
                self.studentList[int(toReplace)-1] = replaceWith
                print("Replaced %s with %s" % (repalacedStudent, replaceWith))
            except:
                print("That student doesn't exist, enter a diffrent student")
        else:
            try:
                self.studentList[self.studentList.index(toReplace)] = replaceWith
                print("Replaced %s with %s" % (toReplace, replaceWith))
            except:
                print("That student doesn't exist, enter a diffrent student")
    
    def removeStudent(self, toRemove):
        if toRemove.isnumeric():
            try:
                self.studentList.pop(int(toRemove)-1)
                print(f"Removed {self.studentList[int(toRemove)-1]} from the list")
            except:
                print("That student doesn't exist, enter a diffrent student")

st = Students()

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

while True:
    menuChoice = input("What would you like to do? ").upper()
    if menuChoice == "ADD":
        newStudent = input("What is the name of the new student? ")
        st.addStudent(newStudent)
    elif menuChoice == "SHOW":
        students = st.getStudents()
        print(f"There are {len(students)} in the class:")
        for i in range(len(students)):
            print(f"{i+1}: {students[i]}")
    elif menuChoice == "UPDATE":
        toReplace = input("What is the name or number of the student to replace? ")
        replaceWith = input("What is the name of the student to replace with? ")
        st.updateStudent(toReplace, replaceWith)
    elif menuChoice == "REMOVE":
        toRemove = input("What is the name or number of the student to remove? ")
        st.removeStudent(toRemove)
    elif menuChoice == "EXIT":
        print("Exiting...")
        break
    else:
        print("That is not a valid option, please type: ADD, SHOW, UPDATE, REMOVE or EXIT")