import threading
from time import sleep,ctime

def music(name,loop):
    for i in range(loop):
        print("I was listening to %s at %s"%(name,ctime()))
        sleep(3)
        print("music was done at %s"%ctime())

def movie(name,loop):
    for i in range(loop):
        print("I was watching  %s at %s"%(name,ctime()))
        sleep(6)
        print("movie was done at %s"%ctime())

if __name__ == "__main__":
    threads = []
    t1 = threading.Thread(target=music,args=("take me to your heart",1))
    t2 = threading.Thread(target=movie,args=("iron man",1))
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("all was end %s"%ctime())
