data = "xibu4xpset beesftt jt pvucpbse.hsje.sfkpjot"

for i in range(-10, 10):
    output = ""
    for character in data:
        output += chr(ord(character)+i)
    print(f"{i = }")
        # print(f"{ord(character) = }")
    print(output)