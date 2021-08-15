#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
import socket
import sys
import threading

class EchoServer (threading.Thread):
    def __init__(self, host, port, bufferSize):
      threading.Thread.__init__(self)
      self.host = host
      self.port = port
      self.bufferSize = bufferSize
      self.exitLoop = False
     
    def run(self):
        print('Thread run started')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            print('Socked address bind')
            s.listen()
            print('Socket listening')
            conn, addr = s.accept()
            print('Waiting for incoming connection')
            with conn:
                try:
                    print('Connected by', addr)
                    while not self.exitLoop:
                        data = conn.recv(int(self.bufferSize))
                        while data:
                            print('Message received: ' + data.decode())  
                            conn.sendall(bytes(data.decode(),'utf-8'))
                            print('Message echoed')
                            data = conn.recv(int(self.bufferSize))
                except ConnectionResetError:
                    print('As it turns out a CorrectionResetError have been catch')
                except ConnectionAbortedError:
                    print('As it turns out a ConnectionAbortedError have been catch')
                finally:
                    conn.close()
                    s.close()
    def exitLoop(self):
        print('Signal caught')
        self.exitLoop = True       

def usage():
    print('python echoServerThreading.py <address> <port> <buffer>')

def main(args):
    if (len(args) != 4):
        usage()
    else: 
        server = EchoServer(args[1], int(args[2]), int(args[3]))
        signal.signal(signal.SIGINT, server.exitLoop)       
        server.start()
    return 0

if __name__ == '__main__': 
    sys.exit(main(sys.argv))
