# Requires Python 2
import random
import time
import thread

DEFAULT_THREADS = 10
DEFAULT_MAX_SLEEP = 5

def threadFunction(identifier, delay):
    print('Hi there, I\'m ', int(identifier), ' and I will sleep for ', delay, ' seconds')
    time.sleep(delay)
    print('Hi there, I\'m ', int(identifier), ' and I just woke up after ', delay, ' seconds')
    
def main(args):
    numberOfThreads = DEFAULT_THREADS
    if len(args) > 1:
        numberOfThreads = int(args[1])
    print('About to created ', numberOfThreads, ' of threads')
    for index in range(0, numberOfThreads):
        delay = random.randrange(DEFAULT_MAX_SLEEP)
        thread.start_new_thread(threadFunction, (index, delay))
    time.sleep(DEFAULT_MAX_SLEEP)
    print('That\'s all folks!')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
