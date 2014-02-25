import socket
import sys
import time
import os
c=1
while(c) :
   if os.path.exists('save.txt'):
      s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
      count=5
      while (count):
          f1=open("save.txt","r")
          data=(f1.read())

          if data.strip():
                  data=int(data)
                  f=open ("hello1.txt", "rb")
                  l = f.read(1024)
                  s.sendto(l,("10.0.0.1",9999))
                  count=count-1
                  time.sleep(data)
      c=0
      s.close()
sys.exit()
