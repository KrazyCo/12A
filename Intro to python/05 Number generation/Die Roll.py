from random import randint

print('Die one is "%s", die two is "%s"' % (randint(1,6), randint(1,6)))

while True:
    input("\nPress enter for another set of numbers")
    print('Die one is "%s", die two is "%s"' % (randint(1,6), randint(1,6)))