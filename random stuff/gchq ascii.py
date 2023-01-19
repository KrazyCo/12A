data = "doov zhoo wkdw hqgv zhoo"

for i in range(0, 26):
    output = ""
    for character in data:
        if ord(character) == 32:
            output += " "
        else:
            if ord(character) < 65 or ord(character) > 122:
                output += character
            elif ord(character)+i > 122:
                output += chr(ord(character)+i-26)
            elif ord(character)+i < 97:
                output += chr(ord(character)+i+26)
            else:
                output += chr(ord(character)+i)
    print(f"{i = }")
        # print(f"{ord(character) = }")
    print(output)