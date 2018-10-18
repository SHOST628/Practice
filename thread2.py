import threading
from time import sleep,ctime

def suplayer(file,time,loop):
    print("start playing %s at %s"%(file,ctime()))
    sleep(time)
    print("%s end at %s"%(file,ctime()))

file_dict = {"love.mp3":6,"iron man.rmvb":3}
threadl = []
print(file_dict.items())

for file,time in file_dict.items():
    t = threading.Thread(target=suplayer,args=(file,time,1))
    threadl.append(t)

if __name__ == "__main__":
    threadl[0].setDaemon(True)
    for t in threadl:
        t.start()
        print(t.getName())
        # t.join()
    # for t in threadl:
    #     t.join()

    print("all is end at %s"%ctime())