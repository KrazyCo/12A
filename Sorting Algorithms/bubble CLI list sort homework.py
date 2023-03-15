import time
import sys


def bubbleSort(list):
    swapped = True
    passNum = 0

    while swapped:
        swapped = False
        passNum += 1
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swapped = True
                # print(list)
                textToPrint = ""
                for e in range(len(list)):
                    if e == i or e == i+1:
                        textToPrint += "_"+str(list[e])+"_ "
                    else:
                        textToPrint += " "+str(list[e])+"  "
                sys.stdout.write("\r"+textToPrint)
                # sys.stdout.write("\n")
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write("\n")
        sys.stdout.flush()


if __name__ == "__main__":
    print("test_list_1:")
    bubbleSort([4, 6, 7, 8, 9, 11, 14, 18, 27, 1])
    print("test_list_2")
    bubbleSort([6, 11, 1, 4, 8, 9, 27, 7, 18, 14])
    print("test_list_3")
    bubbleSort([8, 6, 27, 11, 18, 14, 9, 4, 7, 1])
    print("test_list_4")
    bubbleSort([9, 4, 8, 11, 7, 6, 18, 27, 14, 1])
    print("reversed_list")
    bubbleSort([27, 18, 14, 11, 9, 8, 7, 6, 4, 1])
