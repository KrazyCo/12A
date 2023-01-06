from createList import createRandomOrderedList

def binarySearch(array, target):
    print(array)
    low, high = 0, len(array)-1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return None


if __name__ == "__main__":
    # print(binarySearch([0, 1, 2, 3, 3, 4, 6, 7, 8, 9], 3))
    print(binarySearch(createRandomOrderedList(20), 3))
    # print(binarySearch(list(range(0,20)), 3))
