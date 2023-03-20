import time

startTime = time.time()

for count in range(0,1000000):
    print(count)
print("finished")
print(time.time() - startTime)
print(f"1 billion would take {(time.time() - startTime) * 1000} seconds")