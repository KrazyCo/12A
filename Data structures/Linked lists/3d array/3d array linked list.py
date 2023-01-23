names = [["Alex BREW", [10]], ["Wil BROOKS", [-1]], ["Andreas KRISTENSEN", [9]], ["Musashi LOWE", [1]], ["Alesandro NOEL", [0]], ["Matvey OSIPOV", [3]], ["Aidan ROLFE", [4]], ["Luke SOUTHALL", [5]], ["Felix STONE", [7]], ["Conor STRICKLAND", [8]], ["Arun SURMAN", [2]]]

startPointer = 6

currentPointer = startPointer

while currentPointer != -1:
    print(names[currentPointer][0])
    currentPointer = names[currentPointer][1][0]