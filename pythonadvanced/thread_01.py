def computer():
    while 1:
        pass

from threading import Thread


t1 = Thread(target=computer)
t2 = Thread(target=computer)
t1.start()
#t2.start()