import time
import sys


def insertSort(list):
        for i in range(len(list)):
            element = list[i]
            j = i
            while (j > 0 and list[j-1] > element):
                list[j] = list[j-1]
                j-=1
        # print(list)
                textToPrint = ""
                for e in range(len(list)):
                    if e == j or e == j+1:
                        textToPrint+="_"+str(list[e])+"_ "
                    else:
                        textToPrint+=" "+str(list[e])+"  "
                sys.stdout.write("\r"+textToPrint)
                # sys.stdout.write("\n")
                sys.stdout.flush()
                time.sleep(0.1)
            list[j] = element
            textToPrint = ""
            for e in range(len(list)):
                if e == j or e == j+1:
                    textToPrint+="_"+str(list[e])+"_ "
                else:
                    textToPrint+=" "+str(list[e])+"  "
            sys.stdout.write("\r"+textToPrint)
            # sys.stdout.write("\n")
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write("\n")
        sys.stdout.flush()

if __name__ == "__main__":
    print("test_list_1:")
    insertSort([4,6,7,8,9,11,14,18,27,1])
    time.sleep(0.5)
    print("test_list_2")
    insertSort([6,11,1,4,8,9,27,7,18,14])
    time.sleep(0.5)
    print("test_list_3")
    insertSort([8,6,27,11,18,14,9,4,7,1])
    time.sleep(0.5)
    print("test_list_4")
    insertSort([9,4,8,11,7,6,18,27,14,1])
    time.sleep(0.5)
    print("reversed_list")
    insertSort([27,18,14,11,9,8,7,6,4,1])