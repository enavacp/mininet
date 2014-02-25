import select
import socket
import sys
import time
size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("",9999))
input = [server]
running =1
while running:
    inputready,outputready,exceptready = select.select(input,[],[])
    for s in inputready:
               l,addr=s.recvfrom(1024)
               t=time.strftime(" %S ")
               x=addr[0]
               sys.stdout.write(str(x))
               sys.stdout.write(" time=%s " %t)
               sys.stdout.write(l)
               na=open("nav.txt","a")
               na.write(str(x))
               na.write(" time=%s " %t)
               na.write(l)
               na.write("\n")
server.close()
sys.exit()
