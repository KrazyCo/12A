import random

def randomise(list):
    random.shuffle(list)
    return list

if __name__ == "__main__":
    print(randomise([1,4,6,7,8,9,11,14,18,27]))