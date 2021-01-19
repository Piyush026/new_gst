# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

import read_excel
from runner import main

lst = read_excel.lst
lst1 = lst[2:100]
lst2 = lst[100:200]
lst3 = lst[200:300]

if __name__ == "__main__":
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
