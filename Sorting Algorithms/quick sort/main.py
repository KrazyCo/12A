def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    array.pop(0)

    leftArray = []
    rightArray = []

    for i in range(0,len(array)):
        if array[i] <= pivot:
            leftArray.append(array[i])
        else:
            rightArray.append(array[i])
    # print(f"{type([pivot]) = }")
    array = quicksort(leftArray) + [pivot] + quicksort(rightArray)
    return array

if __name__ == "__main__":
    # test code
    testarrs = [[],
                [2],
                [1, 5],
                [5, 1],
                [1, 6, 2],
                [6, 2, 1],
                [9, 8, 7, 6, 5, 4, 3, 2, 1],
                [1, 18, 7, 9, 8, 4, 2, 6, 0, 14, 19, 16, 11, 12, 15, 5, 13, 17, 3, 10]]

    print(f"{testarrs[-1] = }")

    for array in testarrs:
        print(array, "-->", quicksort(array))
