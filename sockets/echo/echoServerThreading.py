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
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            try:
                conn, addr = s.accept()
                print('Waiting for incoming connection')
                with conn:
                    print('Connected by', addr)
                    while not self.exitLoop:
                        data = conn.recv(int(self.bufferSize))
                        print('Message received: ' + data.decode())  
                        conn.sendall(bytes(data.decode() + ' ','utf-8'))
                        print('Message echoed')
            except ConnectionResetError:
                print('As it turns out a CorrectionResetError have been catch')
                    
    def exitLoop(self):
        self.exitLoop = True       

def main(args):
    server = EchoServer(args[1], int(args[2]), int(args[3]))
    signal.signal(signal.SIGINT, server.exitLoop)       
    server.start()
    return 0

if __name__ == '__main__': 
    sys.exit(main(sys.argv))
