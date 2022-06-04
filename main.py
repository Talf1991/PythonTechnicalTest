import threading
import time
import random
import queue
import ConsumerThread

mutex = threading.Lock()

def CheckInputUser(text):
    while True:
        inputFromUser = input(text)

        if inputFromUser.strip().isdigit() and int(inputFromUser) > 0:
            return inputFromUser

        else:
            print("Input incorrect, please try again")


if __name__ == '__main__':
    count = ConsumerThread.Count()
    consumerQueue = queue.Queue()
    consumerQueue.put(0)
    consumerQueue.put(1)
    consumerQueue.put(2)
    consumerQueue.put(3)
    consumerQueue.put(4)
    consumerQueue.put(5)
    consumerQueue.put(6)
    consumerQueue.put(7)
    consumerQueue.put(8)
    consumerQueue.put(9)

    numberConsumers = int(CheckInputUser('Enter the number of consuming threads: '))
    consumers = [ConsumerThread.ConsumerThread(mutex, consumerQueue, count)  for i in range(numberConsumers)]
    for consumer in consumers: 
        consumer.start()
    waiting = True
    
    while waiting:
        if consumerQueue.empty():
            waiting = False
            
    for consumer in consumers: 
        consumer.join()
