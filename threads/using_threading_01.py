import random
import time
import threading

DEFAULT_THREADS = 10
DEFAULT_MAX_SLEEP = 5


class delayThread (threading.Thread):
    def __init__(self, threadID, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.delay = delay
      
    def threadFunction(self, identifier, delay):
        print('Hi there, I\'m ', identifier, ' and I will sleep for ', delay, ' seconds')
        time.sleep(delay)
        print('Hi there, I\'m ', identifier, ' and I just woke up after ', delay, ' seconds')      
      
    def run(self):
      print("Starting ",self.threadID)
      self.threadFunction(self.threadID, self.delay)
      print("Exiting ", self.threadID)
         
def main(args):
    numberOfThreads = DEFAULT_THREADS
    if len(args) > 1:
        numberOfThreads = int(args[1])
    print('About to created ', numberOfThreads, ' of threads')
    threads = []
    for index in range(0, numberOfThreads):
        delay = random.randrange(DEFAULT_MAX_SLEEP)
        threads.append(delayThread(index, delay))
    print('Created ', numberOfThreads, ' threads')
    print('About to start ', numberOfThreads, ' of threads')
    for currentDelayThread in threads:
        currentDelayThread.start()    
    print('Started ', numberOfThreads, ' threads')    
    time.sleep(DEFAULT_MAX_SLEEP)
    print('That\'s all folks!')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
