import datetime;
import random;

def main(args):
    randomIntegersUpperLimit = int(args[2])
    file = open(args[1], 'w')
    t0 = datetime.datetime.now().timestamp()    
    for index in range(randomIntegersUpperLimit):
        file.write(str(random.randrange(randomIntegersUpperLimit)) + "\n")
    t1 = datetime.datetime.now().timestamp()
    print("Python generated " + args[2] + " pseudo random integers in " + str((t1 - t0) * 1000) + "ms. and saved them to: " + args[1])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))