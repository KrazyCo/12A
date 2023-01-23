names = ["Alex BREW","Wil BROOKS", "Andreas KRISTENSEN", "Musashi LOWE", "Alesandro NOEL", "Matvey OSIPOV", "Aidan ROLFE", "Luke SOUTHALL", "Felix STONE", "Conor STRICKLAND", "Arun SURMAN"]

pointers = [10, -1, 9, 1, 0, 3, 4, 5, 7, 8, 2]

startPointer = 6

end = False
currentPointer = startPointer
while end == False:
    print(names[currentPointer])
    currentPointer = pointers[currentPointer]
    if startPointer == -1:
        end = True