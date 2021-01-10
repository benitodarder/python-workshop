import sys
import socket

def main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((args[1], int(args[2])))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            received = ''
            while True:
                data = conn.recv(1024)
                if not data:
                    break            
                received = received + data.decode()
        print('Message received: ' + received)  
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
