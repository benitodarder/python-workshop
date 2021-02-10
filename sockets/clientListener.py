# Sends arguments, from the third and onwards, to the serverListener.py
import sys
import socket

def main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args[1], int(args[2])))
        received = ''
        while True:
            data = s.recv(1024)
            if not data:
                break            
            received = received + data.decode()
        print('Message received: ' + received)  
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
