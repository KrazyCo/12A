from mergeArrays import mergeArrays

def mergeSort(array):
    if len(array) <= 1: return array 
    leftArray = array[0:len(array)//2]
    rightArray = array[len(array)//2:]
    
    sortedLeft = mergeSort(leftArray)
    sortedRight = mergeSort(rightArray)

    sortedArray = mergeArrays(sortedLeft, sortedRight)

    return sortedArray

if __name__ == "__main__":
    testArrays = [[],
                [2],
                [1, 5],
                [5, 1],
                [1,6,2],
                [6,2,1],
                [9, 8, 7, 6, 5, 4, 3, 2, 1]]
    for array in testArrays:
        print(array, "-->", mergeSort(array))