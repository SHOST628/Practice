import  threading
import time
from time import sleep
def music(name):
    print("%s begin listening to music %s"%(name,time.ctime()))
    sleep(3)
    print("%s stop listning to music %s"%(name,time.ctime()))

def game(name):
    print("%s begin playing game %s"%(name,time.ctime()))
    sleep(3)
    print("%s stop playing game %s"%(name,time.ctime()))

if __name__ == "__main__":
    Thread1 = threading.Thread(target=music,args=('SZ',))
    Thread2 = threading.Thread(target=game,args=('SZ',))
    Thread1.start()
    Thread2.start()
    print("Ending at %s"%(time.ctime()))





