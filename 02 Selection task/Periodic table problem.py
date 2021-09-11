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
userInput = str(input("Enter the symbol or name of an element: "))

print('''
Element: %s(%s)
Atomic weight: %s
Group: %s''' % (elements[userInput.lower()][0], elements[userInput.lower()][1], elements[userInput.lower()][2], elements[userInput.lower()][3]))
    
    # elements[userInput.lower()][0])