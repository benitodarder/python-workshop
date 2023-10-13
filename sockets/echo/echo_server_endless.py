#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
import socket
import sys
import threading
import os

exitLoop = False

class EchoServer (threading.Thread):
    def __init__(self, bufferSize, listeningConnection):
      threading.Thread.__init__(self)
      self.bufferSize = bufferSize
      self.listeningConnection = listeningConnection
      self.exitLoop = False

     
    def run(self):
        print('Thread run started with pid: ' + str(os.getpid()))
        with self.listeningConnection:
            try:
                data = self.listeningConnection.recv(int(self.bufferSize))
                while data:
                    print('Message received: ' + data.decode())  
                    self.listeningConnection.sendall(bytes(data.decode(),'utf-8'))
                    print('Message echoed')
                    data = self.listeningConnection.recv(int(self.bufferSize))
            except ConnectionResetError:
                print('As it turns out a CorrectionResetError have been catch')
            except ConnectionAbortedError:
                print('As it turns out a ConnectionAbortedError have been catch')
            finally:
                self.listeningConnection.close()

def exitLoop():
    global exitLoop
    exitLoop = True       

def usage():
    print('python echoServerThreading.py <address> <port> <buffer>')

def main(args):
    if (len(args) != 4):
        usage()
    else:
        exitLoop = False
        signal.signal(signal.SIGINT, exitLoop)       
        print("Echo server pid: " + str(os.getpid()))
        while not exitLoop:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as inputSocket:
                inputSocket.bind((args[1], int(args[2])))
                inputSocket.listen()
                conn, addr = inputSocket.accept()   
                print('Connected by', addr)        
                server = EchoServer(int(args[3]), conn) 
                server.start()
    return 0

if __name__ == '__main__': 
    sys.exit(main(sys.argv))
