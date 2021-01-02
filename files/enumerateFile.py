def main(args):
    file = open(args[1], 'r')
    for index, line in enumerate(file):
        print(index, ' : ' + line)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))