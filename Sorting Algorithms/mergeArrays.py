def mergeArrays(array1, array2):
    arr1Pos = arr2Pos = newArrPos = 0
    newArray = [None] * (len(array1) + len(array2))
    for i in range(0, len(newArray)):
        if arr1Pos == len(array1):
            if arr2Pos != len(array2):
                newArray[newArrPos] = array2[arr2Pos]
                arr2Pos += 1
                newArrPos += 1
        elif arr2Pos == len(array2):
            if arr1Pos != len(array1):
                newArray[newArrPos] = array1[arr1Pos]
                arr1Pos += 1
                newArrPos += 1
        else:
            if array1[arr1Pos] <= array2[arr2Pos]:
                newArray[newArrPos] = array1[arr1Pos]
                arr1Pos += 1
                newArrPos += 1
            else:
                newArray[newArrPos] = array2[arr2Pos]
                arr2Pos += 1
                newArrPos += 1
    return newArray

if __name__ == "__main__":
    arr1 = [1,5,7,9,15,17]
    arr2 = [2,3,4,8,12,16,19]
    print(mergeArrays(arr1, arr2))