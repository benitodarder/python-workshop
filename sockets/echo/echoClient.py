#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
            dataSentLength = 0
            for index, current in enumerate(args):
                if index > 3:
                    dataSentLength = dataSentLength + len(current)
                    s.send(bytes(current + ' ','utf-8'))  
            print('Message sent')
            dataReceivedLength = 0
            while dataReceivedLength < dataSentLength:
                data = s.recv(int(args[3]))
                dataReceivedLength = dataReceivedLength + len(data)
                print('Message received: \'' + data.decode() + '\'')  
            s.shutdown(socket.SHUT_RDWR)
            s.close()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
