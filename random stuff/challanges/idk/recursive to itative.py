def calculate(num1, num2):
    while num1 != num2:
        if num1 < num2:
            num2 = num2-num1
        else:
            num1, num2 = num2, num1-num2
    return num1

def recursiveCalculate(num1, num2):
    if num1 == num2:
        return num1
    elif num1 < num2:
        return calculate(num1, num2-num1)
    else:
        return calculate(num2, num1,num2)

print(f"{calculate(1,10) = }")
print(f"{recursiveCalculate(1,10) = }")
