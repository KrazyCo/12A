import random

def createRandomOrderedList(length):
    output = [0]*length
    for i in range(len(output)):
        output[i] = random.randint(0,length-1)
    output.sort()
    return output

if __name__ == "__main__":
    print(createRandomOrderedList(25))