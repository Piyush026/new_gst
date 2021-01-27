import threading
import time
# import read_excel
from concurrent.futures import ThreadPoolExecutor
from csvRead import tuples
# lst = readfile()
lst = tuples[:50]
from runner import main
#
# lst = read_excel.lst
# lst1 = lst[2:100]
# lst2 = lst[100:200]
# lst3 = lst[200:300]

if __name__ == "__main__":
    start_time = time.time()
    print(start_time)
    with ThreadPoolExecutor(max_workers=8) as executor:
        future = executor.map(main, lst)
        # future1 = executor.map(maain, data2)
        # # future2 = executor.map(maain, data3)
    duration = time.time() - start_time
    print(f"data  in {duration} seconds")

