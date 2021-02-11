# Read echoed message
import sys
import socket

def usage():
    print('python echoClient.py <address> <port> <buffer> <messages>')

def main(args):
    if (len(args) <= 4):
        usage()
    else:    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((args[1], int(args[2])))
            for index, current in enumerate(args):
                if index > 3:
                    s.send(bytes(current + ' ','utf-8'))  
            print('Message sent')
            data = s.recv(int(args[3]))
            print('Message received: ' + data.decode())  
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
