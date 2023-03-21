# import time

# startTime = time.time()

# for count in range(0,1000000):
#     print(count)
# print("finished")
# print(time.time() - startTime)
# print(f"1 billion would take {(time.time() - startTime) * 1000} seconds")

number = 2

for i in range(0,4100):
    number = number * 2

print(number)
print(len(str(number)))

# number = 2

# for i in range(0,20): # this loop will never finish lmao
#     number = number * number
#     print(number)
#     print(f"{i = }")
#     print(f"{len(str(number)) = }")