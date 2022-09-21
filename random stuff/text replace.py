import sys
import time

for i in range(10):
    sys.stdout.write(f"\rDoing thing {i}")
    time.sleep(0.2)
    # sys.stdout.flush()