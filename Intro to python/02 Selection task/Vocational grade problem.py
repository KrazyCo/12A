while True:
    score = int(input("Enter your mark out of 100: "))
    if score <= 100:
        break
    else:
        print("The score must be below 100")

if score < 40:
    grade = "Fail"
elif score < 60:
    grade = "Pass"
elif score < 80:
    grade = "Merit"
else:
    grade = "Distiction"

print("You scored a " + grade)