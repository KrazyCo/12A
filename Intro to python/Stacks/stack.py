class Stack:
    def __init__(self,length):
        self.length = length
        self.index = 0
        self.stack = [""]*length
    
    def push(self, arg):
        if self.index >= self.length:
            return 
        self.stack[self.index] = arg
        self.index += 1

    def pop(self):
        if self.index == 0:
            return
        self.index -= 1
        return self.stack[self.index]

    def peek(self):
        if self.index == 0:
            return
        return self.stack[self.index-1]

    def printStack(self):
        for i in range(self.length-1, self.index-1, -1):
            print(str(i) + ":")
        for i in range(self.index-1, -1, -1):
            print(str(i) + ":", self.stack[i])

if __name__ == "__main__":
    stack = Stack(10)
    while True:
        userInput = str(input("0 for push, 1 for pop, 2 for peek, 3 for printStack: "))
        if userInput[0] == "0":
            stack.push(userInput[2:])
        if userInput[0] == "1":
            print(stack.pop())
        if userInput[0] == "2":
            print(stack.peek())
        if userInput[0] == "3":
            stack.printStack()