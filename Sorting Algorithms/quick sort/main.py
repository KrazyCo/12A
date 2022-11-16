def quicksort(array):
    leftArray, rightArray, pivot, end, oarray, array = ([], [], array.pop(0) if len(array)>1 else 0, False if len(array)>1 else True, array, array if len(array)>1 else [])
    for i in range(0,len(array)): leftArray.append(array[i]) if array[i] <= pivot else rightArray.append(array[i])
    return quicksort(leftArray) + [pivot] + quicksort(rightArray) if not end else oarray

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

    # print(f"{testarrs[-1] = }")

    for arr in testarrs:
        print(arr, "-->", quicksort(arr))
