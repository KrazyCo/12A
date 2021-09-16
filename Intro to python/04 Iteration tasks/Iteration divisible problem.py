while True:
  num1 = int(input("What is your number to divide by? "))
  num2 = int(input("What is your number to divide? "))

  if num1 == 0 or num2 == 0:
    print("Error: you cannot divide by 0, please enter another set of numbers without 0")
  else:
    if num2%num1 == 0:
      print("%s is exactly divisible by %s" % (num2, num1))
    else:
      print("%s is not exactly divisible by %s, there is a remainder of %s" % (num2, num1, num2%num1))
    break