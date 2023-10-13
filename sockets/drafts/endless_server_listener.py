# Reads endlessly until SIGINT
import sys
import socket
import signal

def signal_handler(signal, frame):
    print("That's all folks!")
    sys.exit(0)

def usage():
    print('python echoServer.py <address> <port> <buffer>')

def main(args):
    if (len(args) != 4):
        usage()
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((args[1], int(args[2])))
        print("Bind: " + args[1] + ":" + args[2])
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(int(args[3]))
                print('From: ', addr, '; Message received: ' + data.decode())  
                conn.sendall(bytes(data.decode() + ' ','utf-8'))  
                print('Message echoed!')  
        s.close()
    return 0

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    sys.exit(main(sys.argv))
