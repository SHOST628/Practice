import threading
from time import sleep,ctime

def suplayer(file,time,loop):
    print("start playing %s at %s"%(file,ctime()))
    sleep(time)
    print("%s end at %s"%(file,ctime()))

file_dict = {"love.mp3":3,"iron man.rmvb":6}
threadl = []
print(file_dict.items())

for file,time in file_dict.items():
    t = threading.Thread(target=suplayer,args=(file,time,1))
    threadl.append(t)

if __name__ == "__main__":
    threadl[1].setDaemon(True)
    for t in threadl:
        t.start()
        # t.join()
    # for t in threadl:
    #     t.join()
    print("all is end at %s"%ctime())