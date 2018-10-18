import multiprocessing
from time import sleep,ctime

def super_player(file,time,loop):
    for l in range(loop):
        print("start playing %s at %s"%(file,ctime()))
        sleep(time)
        print("%s end at %s"%(file,ctime()))

file_dict = {"love.mp3":3,"iron man.rmvb":6}
threads = []

for file,time in file_dict.items():
    p = multiprocessing.Process(target=super_player,args=(file,time,1))
    threads.append(p)

if __name__ == "__main__":
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("all is end at %s"%ctime())