#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
import socket
import sys
import threading
import os

class EchoClient (threading.Thread):
    def __init__(self, host, port, bufferSize):
      threading.Thread.__init__(self)
      self.host = host
      self.port = port
      self.bufferSize = bufferSize
      self.exitLoop = False
     
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as outputSocket:
            print("Current pid: " + str(os.getpid()))
            outputSocket.connect((self.host, self.port))
            try:
                while not self.exitLoop:
                    current = input('Message: ')
                    outputSocket.sendall(bytes(current,'utf-8'))  
                    dataSentLength = len(current)
                    dataReceivedLength = 0
                    while dataReceivedLength < dataSentLength:
                        data = outputSocket.recv(int(self.bufferSize))
                        dataReceivedLength = dataReceivedLength + len(data)
                        print('Message received: \'' + data.decode() + '\'')               
            except ConnectionResetError:
                print('As it turns out a CorrectionResetError have been catch')
            finally:
                outputSocket.shutdown(socket.SHUT_RDWR)
                outputSocket.close()
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
