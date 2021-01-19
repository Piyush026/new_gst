import threading
import time
from concurrent.futures import ThreadPoolExecutor
from gst import readfile, maain
from csvRead import tuples
# lst = readfile()
lst = tuples[:300000]

print(len(lst))
if __name__ == "__main__":
    start_time = time.time()
    print(start_time)
    with ThreadPoolExecutor(max_workers=8) as executor:
        future = executor.map(maain, lst)
        # future1 = executor.map(maain, data2)
        # # future2 = executor.map(maain, data3)
    duration = time.time() - start_time
    print(f"data  in {duration} seconds")


