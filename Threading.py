from threading import Thread
import time

Numbers = ["1","2","3","4","5","6","7","8","9","10"]

def function2(name):
    counter = 0
    while True:
        counter += 1
        print("Hello, first thread here, {0}\n".format(counter))
        time.sleep(2)

def function1(name):
    counter = 0
    while True:
        counter += 1
        print("I'm the second thread, {0}\n".format(counter))
        time.sleep(3)

MyThread = Thread(target=function1, args=(1,))
MyThread2 = Thread(target=function2, args=(1,))

MyThread2.start()
MyThread.start()
