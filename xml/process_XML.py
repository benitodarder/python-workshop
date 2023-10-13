import xml.etree.ElementTree as ET
def main(args):
    inputFile = ET.parse(args[1])
    root = inputFile.getroot()
    walkThroughNode(root)
    return 0

def walkThroughNode(node):
    if (node.text):
        print(node.tag, node.text)
    else:
        print(node.tag)
    printAttributes(node.attrib)
    for child in node:
        walkThroughNode(child)    
            
def printAttributes(attribs):
    for key in attribs:
        print("    key: " + key + ", value: " + attribs[key])

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))