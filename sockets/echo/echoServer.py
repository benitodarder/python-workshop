# Echoes recieved message
import sys
import socket

def usage():
    print('python echoServer.py <address> <port> <buffer>')

def main(args):
    if (len(args) != 4):
        usage()
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((args[1], int(args[2])))
            print("Bind: " + args[1] + ":" + args[2])
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(int(args[3]))
                print('Message received: ' + data.decode())  
                conn.sendall(bytes(data.decode() + ' ','utf-8'))  
                print('Message echoed!')  
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
