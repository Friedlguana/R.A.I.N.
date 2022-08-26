#Module Import
import platform
import os
import socket

#Variable Assignment
Platform = platform.system()

#Function 1
def clear():
  if Platform == 'Linux':
    os.system("clear")

  elif Platform == 'Windows':
    os.system("cls")

#Function 2
target = "127.0.0.1"
OpenPorts = []
def port_scanner(Port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, Port))
        print(f"Port {Port} is open")
        OpenPorts.append(Port)
    except:
        pass