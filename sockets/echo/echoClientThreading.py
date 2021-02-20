#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
import socket
import sys
import threading

class EchoClient (threading.Thread):
    def __init__(self, host, port, bufferSize):
      threading.Thread.__init__(self)
      self.host = host
      self.port = port
      self.bufferSize = bufferSize
      self.exitLoop = False
     
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            try:
                while not self.exitLoop:
                    current = input('Message: ')
                    s.sendall(bytes(current + ' ','utf-8'))  
                    data = s.recv(self.bufferSize)
                    print('Message received: ' + data.decode())               
            except ConnectionResetError:
                print('As it turns out a CorrectionResetError have been catch')
                
    def exitLoop(self):
        self.exitLoop = True

def usage():
    print('python echoClientThreading.py <address> <port> <buffer>')

def main(args):
    if (len(args) != 4):
        usage()
    else:      
        server = EchoClient(args[1], int(args[2]), int(args[3]))
        signal.signal(signal.SIGINT, server.exitLoop)    
        server.start()    
    return 0

if __name__ == '__main__': 
    sys.exit(main(sys.argv))
