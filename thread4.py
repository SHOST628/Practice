import threading
from time import sleep

thread_local =threading.local()
# lock = threading.RLock()

def show():
    print(threading.current_thread().getName()," ",thread_local.num)

def func(arg):
    # lock.acquire()
    thread_local.num = arg
    for i in range(10):
        thread_local.num += 1
    show()
    # lock.release()
if __name__ == "__main__":
    for i in range(2):
        t = threading.Thread(target=func,args=(i,))
        t.start()
        # print(t.isAlive())
        # t.join()
    print("end")



