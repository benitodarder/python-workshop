# Reads message from serverWriter.py
import sys
import socket

def main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args[1], int(args[2])))
        for index, current in enumerate(args):
            if index > 2:
                s.sendall(bytes(current + ' ','utf-8'))  
        print('Message sent')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
