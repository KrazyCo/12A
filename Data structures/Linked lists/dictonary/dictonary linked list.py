namesDictionary = {"Alex BREW":"Arun SURMAN","Wil BROOKS":"null", "Andreas KRISTENSEN":"Conor STRICKLAND", "Musashi LOWE":"Wil BROOKS", "Alesandro NOEL":"Alex BREW",
"Matvey OSIPOV":"Musashi LOWE", "Aidan ROLFE":"Alesandro NOEL", "Luke SOUTHALL":"Matvey OSIPOV", "Felix STONE":"Luke SOUTHALL", "Conor STRICKLAND":"Felix STONE", "Arun SURMAN":"Andreas KRISTENSEN"}

currentPointer = "Aidan ROLFE"

while currentPointer != "null":
    print(currentPointer)
    currentPointer = namesDictionary[currentPointer]