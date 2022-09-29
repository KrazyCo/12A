import random

def generateUsername(firstName, lastName, dob):

    dobstr = str(dob[0:2])+str(dob[3:5])+str(dob[6:10])
    username = firstName[:3]
    username += dobstr[random.randint(0,7)]
    username += dobstr[random.randint(0,7)]
    username += lastName[-3:]
    username += str(dob[0:2])+str(dob[3:5])+str(dob[8:10])

    print(username)

if __name__ == "__main__":
    print(generateUsername("John", "Smith", "12/03/1989"))