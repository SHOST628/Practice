import threading
from time import sleep,ctime

# new threading class

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def super_player(file,time,loop):
    for l in range(loop):
        print("start playing %s at %s"%(file,ctime()))
        sleep(time)
        print("%s end at %s"%(file,ctime()))

file_dict = {"love.mp3":3,"iron man.rmvb":6}
threads = []

for file,name in file_dict.items():
    t = MyThread(super_player,(file,name,1),super_player.__name__)
    threads.append(t)


if __name__ == "__main__":
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("all is end at %s"%(ctime()))



