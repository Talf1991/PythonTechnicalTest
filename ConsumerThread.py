import threading
import time
from threading import Semaphore
import queue

class Count:
    count = 0

class ConsumerThread(threading.Thread):
    def __init__(self, mutex, consumerQueue, count):
        super(ConsumerThread,self).__init__()
        self.mutex = mutex
        self.consumerQueue = consumerQueue
        self.count = count
        self._stop = threading.Event()
        return

    def printNumber(self, number):
        print(threading.current_thread().name
            +' Consuming ' + str(number) + 
            ' : ' + 'Count = ' + str(self.count.count))
        return

    def run(self):
        while True:
            if not self.consumerQueue.empty():
                self.mutex.acquire()
                try:
                    number = self.consumerQueue.get()
                    self.count.count += number
                    ConsumerThread.printNumber(self, number)
                finally:
                    self.mutex.release()
            else:
                self._stop.set()
                 
