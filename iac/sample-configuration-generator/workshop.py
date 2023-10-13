import sys
import re

from variables import Variable

VARIABLE_START = 'variable ".*"'

def main(args):
    print("Testing... Testing...")
    oneVariable = Variable('var name', 'var type', [], None)
    print("We create a variable... This one: ")
    print(oneVariable)
    anotherVariable = Variable('var name too', 'var type too', [], None)
    variables = [oneVariable, anotherVariable]
    print("Several variables in a list...")
    print(variables)
    anotherVariableToo = Variable('That''s a big one...', 'var type too', variables, None)
    print("Let's see a variable with fields...")
    print(anotherVariableToo)
    if len(args) > 1:
        inputFile = open(args[1], 'r')    
        for line in inputFile:
            match = re.search(VARIABLE_START, line)
            if match:
                print(f"New variable start: {line}")
    print("That's all...")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))


