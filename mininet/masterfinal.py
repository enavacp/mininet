import socket,os
import sys
import time
from time import sleep
import threading
import Queue

n=int(sys.argv[1])
#print n
s=[]
HN=[]
l=4
k=2
debug_mode=1

def send_tick_to_all(s,sm):
    print("***Sending Tick****")
    sm.sendto(str(l),("/simhost"))
   # time.sleep(1)
    for i in range(0,n-2):
        s[i].sendto(str(l),("/hostnew%s"%(i+1)))


def send(in_q):

         for i in range(0,n-2):
             s.append(socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM))

         sm=socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM)

         global debug_mode
         while(1):

            if debug_mode:
               data=in_q.get()
               if data== 's':
                  send_tick_to_all(s,sm)
               elif data=='c':
                  send_tick_to_all(s,sm)
               elif data=='h':
                  pass

            else:
               send_tick_to_all(s,sm)
               time.sleep(1)




         sm.close()
         os.remove('/simhost')


         for i in range(0,n-2):
             s[i].close()




def receive(out_q):
    sr=socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM)
    sr.bind("/home/mininet/master")
    global debug_mode
    while(1):
      print "waitinggggggggggg"
#     l,addr=sr.recvfrom(1024)
      if debug_mode :
         l,addr=sr.recvfrom(1024)

         if l=='c':
               debug_mode=0
               sys.stdout.write(l)
               out_q.put(l)
         elif l=='s':
               sys.stdout.write(l)
               out_q.put(l)


         elif l=='h':
              # out_q.put(l)
              pass

      else:
         l,addr=sr.recvfrom(1024)
         if l=='c':
              pass

         elif l=='s':
              pass


         elif l=='h':
              debug_mode=1
              out_q.put(l)



def terminate(self):
    self.stop.set()


q=Queue.Queue()

t1=threading.Thread(target=receive,args=(q,))
t2=threading.Thread(target=send,args=(q,))

t1.start()
t2.start()
#time.sleep(20)
#t1.terminate()
#t2.terminate()   
#os.remove('/home/mininet/master')
sys.exit()
