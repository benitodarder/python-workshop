def main(args):
    inputFile = open(args[1], 'r')
    outputFile = open(args[2], 'w', newline='\n')
    for line in inputFile:
        outputFile.write(line)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))