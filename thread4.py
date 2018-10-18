import threading
from time import sleep

num = 0
# lock = threading.RLock()

def func(arg):
    # lock.acquire()
    global num
    sleep(1)
    num +=1
    print(num)
    # lock.release()

for i in range(10):
    t = threading.Thread(target=func,args=(i,))
    t.start()
    # t.join()
print("end")


