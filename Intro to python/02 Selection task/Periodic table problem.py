# I didn't know how to seach through the dictionary for groups, so I didn't include this

elements = {
    "lithium": ("Lithium", "Li", "6.94", "Alkali metals"),
    "li": ("Lithium", "Li", "6.94", "Alkali metals"),
    "sodium": ("Sodium", "Na", "22.990", "Alkali metals"),
    "na": ("Sodium", "Na", "22.990", "Alkali metals"),
    "potassium": ("Potassium", "K", "39.098", "Alkali metals"),
    "k": ("Potassium", "K", "39.098", "Alkali metals"),
    "helium": ("Helium", "He", "4.003", "Nobel gasses"),
    "he": ("Helium", "He", "4.003", "Nobel gasses"),
    "neon": ("Neon", "Ne", "20.180", "Nobel gasses"),
    "ne": ("Neon", "Ne", "20.180", "Nobel gasses"),
    "argon": ("Argon", "Ar", "39.95", "Nobel gasses"),
    "ar": ("Argon", "Ar", "39.95", "Nobel gasses"),
}
print("Compatible elements: Lithium, Sodium, Potassium, Helium, Neon, Argon\n")
userInput = str(input("Enter the symbol or name of an element, or the group name or number (0 or 1): "))

if userInput == "1" or userInput.lower() == "alkali metals":
    print('''Group 1 (Alkali metals) has:

Element: Lithium(Li)
Atomic weight: 6.94
Group: Alkali metals

Element: Sodium(Na)
Atomic weight: 22.990
Group: Alkali metals

Element: Potassium(K)
Atomic weight: 39.098
Group: Alkali metals''')
elif userInput == "0" or userInput.lower() == "nobel gasses":
    print('''Group 0 (Nobel gasses) has:

Element: Helium(He)
Atomic weight: 4.003
Group: Nobel gasses

Element: Neon(Ne)
Atomic weight: 20.180
Group: Nobel gasses

Element: Argon(Ar)
Atomic weight: 39.95
Group: Nobel gasses''')
else:
    print('''
Element: %s(%s)
Atomic weight: %s
Group: %s''' % (elements[userInput.lower()][0], elements[userInput.lower()][1], elements[userInput.lower()][2], elements[userInput.lower()][3]))