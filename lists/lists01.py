
NUMBER_OF_ELEMENTS=5

def main(args):
    elements = []
    
    for i in range(NUMBER_OF_ELEMENTS):
        elements.append(i)    
    
    print("Initial list: " + str(elements))
    
    print("Iterate through the list in reverse order and pop element.")
    for i in reversed(range(NUMBER_OF_ELEMENTS)):
        print("Removing index: " + str(i) + ", value: " + str(elements.pop()))
        elements.append(i)
    
    print("List after poping" + str(elements))
    
    print("Iterate through the list in reverse order and pop last element.")
    for i in reversed(range(NUMBER_OF_ELEMENTS)):
        print("Removing index: " + str(i) + ", value: " + str(elements.pop()))
        elements.append(i)
    
    print("List after poping" + str(elements))   
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
