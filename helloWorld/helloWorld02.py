
def main(args):
    print('Hello world inception... I am ' + __name__)
    print("About to call helloWorld01.py:")
    helloWorld01.main(args)
    return 0

if __name__ == '__main__':
    import sys
    import helloWorld01
    sys.exit(main(sys.argv))
