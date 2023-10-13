# Reads message from console and sends to given server
import sys
import socket
import signal

def signal_handler(signal, frame):
    print("That's all folks!")
    sys.exit(0)

def usage():
    print('python echoClient.py <address> <port> <buffer>')

def main(args):
    if (len(args) != 4):
        usage()
    else:    
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((args[1], int(args[2])))            
            current = input('Message: ')
            s.sendall(bytes(current + ' ','utf-8'))  
            print('Message sent')
            data = s.recv(int(args[3]))
            print('Message received: ' + data.decode())  
            s.close()
    return 0

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    sys.exit(main(sys.argv))

