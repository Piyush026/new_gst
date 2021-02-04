import threading
import time
# import read_excel
from concurrent.futures import ThreadPoolExecutor
from csvRead import tuples
# lst = readfile()
lst = tuples[50:]
from runner import main
#
# lst = read_excel.lst
lst1 = lst[675:1500]
lst2 = lst[1500:3000]
lst3 = lst[3000:400]

if __name__ == "__main__":
    start_time = time.time()
    print(start_time)
    t1 = threading.Thread(target=main, args=(lst1,))
    t2 = threading.Thread(target=main, args=(lst2,))
    t3 = threading.Thread(target=main, args=(lst3,))

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    print("Done!")
    #with ThreadPoolExecutor(max_workers=1) as executor:
     #   future = executor.map(main, lst)
        # future1 = executor.map(maain, data2)
        # # future2 = executor.map(maain, data3)
    duration = time.time() - start_time
    print(f"data  in {duration} seconds")

