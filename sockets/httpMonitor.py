#!/usr/bin/env python
# -*- coding: utf-8 -*-
CONTENT_LENGTH="Content-Length: "
CHAR_CR="\r"
CHAR_LF="\n"
HEADER_BODY_SEPARATOR=CHAR_CR + CHAR_LF

import signal
import socket
import sys
import threading
import os



class HTTPMonitor (threading.Thread):

  def __init__(self, hostIN, portIN, hostOUT, portOUT, bufferSize):
    threading.Thread.__init__(self)
    self.hostIN = hostIN
    self.portIN = portIN
    self.hostOUT = hostOUT
    self.portOUT = portOUT
    self.bufferSize = bufferSize
    self.exitLoop = False
     
  def run(self):
    print('Thread run started')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as inputSocket, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as outpuSocket:
      print("Current pid: " + str(os.getpid()))
      inputSocket.bind((self.hostIN, self.portIN))
      print('Input socked address bind')
      outpuSocket.connect((self.hostOUT, self.portOUT))
      print('Output socket connected')
      inputSocket.listen()
      print('Input socket listening')
      connIN, addr = inputSocket.accept()
      print('Waiting for incoming connection')
      with connIN:
        try:
          print('Connected by', addr)
          while not self.exitLoop:
            print('Waiting for request... ')
            message = []
            line = ""
            body = ""
            contentLength = 0
            while len(message) == 0 or message[len(message)-1] != HEADER_BODY_SEPARATOR:
              char = connIN.recv(1).decode()
              line = line + char
              if char == CHAR_CR:
                char = connIN.recv(1).decode()
                line = line + char
                if char == CHAR_LF:
                  message.append(line)
                  if line.startswith(CONTENT_LENGTH):
                    contentLength = line[len(CONTENT_LENGTH)::].strip()
                  line = ""
            for i in range(0, int(contentLength)):
              body = body + connIN.recv(1).decode()    
            print("***********************************************************************************************")          
            print("- Request headers: ");
            for i,line in enumerate(message):
              print(line, end="")
            print("- Request body:\n" + body, end="")            
            for i,line in enumerate(message):
              outpuSocket.sendall(bytes(line,'utf-8'))
            outpuSocket.sendall(bytes(body,'utf-8'))
            print("-----------------------------------------------------------------------------------------------")
            print('Message sent to target...')
            print('Waiting for response...')
            print("-----------------------------------------------------------------------------------------------")
            message = []
            line = ""
            body = ""
            contentLength = 0
            while len(message) == 0 or message[len(message)-1] != HEADER_BODY_SEPARATOR:
              char = outpuSocket.recv(1).decode()
              line = line + char
              if char == CHAR_CR:
                char = outpuSocket.recv(1).decode()
                line = line + char
                if char == CHAR_LF:
                  message.append(line)
                  if line.startswith(CONTENT_LENGTH):
                    contentLength = line[len(CONTENT_LENGTH)::].strip()
                  line = ""
            for i in range(0, int(contentLength)):
              body = body + outpuSocket.recv(1).decode()            
            print("- Response headers: ");
            for i,line in enumerate(message):
              print(line, end="")
            print("- Response body:\n" + body, end="")            
            for i,line in enumerate(message):
              connIN.sendall(bytes(line,'utf-8'))
            connIN.sendall(bytes(body,'utf-8'))   
            print("\n***********************************************************************************************")
        except ConnectionResetError:
          print('As it turns out a CorrectionResetError have been catch')
        except ConnectionAbortedError:
          print('As it turns out a ConnectionAbortedError have been catch')
        finally:
          inputSocket.close()
          outpuSocket.close()

  def exitLoop(self):
    print('Signal caught')
    self.exitLoop = True       

def usage():
  print('python HTTPMonitor.py <source address> <source port> <destination address> <destination port> <buffer>')

def main(args):
  if (len(args) != 6):
    usage()
  else: 
    server = HTTPMonitor(args[1], int(args[2]), args[3], int(args[4]), int(args[5]))
    signal.signal(signal.SIGINT, server.exitLoop)       
    server.start()
  return 0

if __name__ == '__main__': 
  sys.exit(main(sys.argv))
