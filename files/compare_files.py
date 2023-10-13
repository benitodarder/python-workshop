def main(args):
    results = []*3
    with open(args[1], 'r') as file01, open(args[2], 'r') as file02:
        lineNumber = 0
        line01 = file01.readline()
        line02 = file02.readline()
        while line01 and line02:
            if line01 != line02:
                results.append((lineNumber, line01, line02))
            line01 = file01.readline()
            line02 = file02.readline()
            lineNumber = lineNumber + 1
        if line01:
            while line01:
                results.append((lineNumber, line01, ''))
                line01 = file01.readline()
                lineNumber = lineNumber + 1
        if line02:
            while line02:
                rresults.append((lineNumber, '', line02))
                line02 = file02.readline()
                lineNumber = lineNumber + 1
    print(len(results), ' differences')           
    for result in results:
        print(result[0], ':', '\n', result[1], result[2]) 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))