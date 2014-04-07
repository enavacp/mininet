import socket
import sys


Seh=socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM)

while(1):
    l=raw_input("Enter The Command : ")
    Seh.sendto(str(l),("/home/mininet/master"))
Seh.close()

os.remove('/home/mininet/master')
