# Writes the arguments, from the third onwards, to the clientListener.py
import sys
import socket

def main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((args[1], int(args[2])))
        print("Bind: " + args[1] + ":" + args[2])
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            for index, current in enumerate(args):
                if index > 2:
                    conn.sendall(bytes(current + ' ','utf-8'))   
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
