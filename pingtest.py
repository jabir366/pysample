import os, re,threading
#received_packages = re.compile(r"(\d) received")
#status = ("no response","alive but losses","alive")
#for suffix in range(0,10):
#    ip = "10.0.2."+str(suffix)
#    ping_out = os.popen("ping -q -c2 "+ip,"r")
#    print "... pinging ",ip
#    while True:
#        line = ping_out.readline()
#        if not line: break
#        n_received = received_packages.findall(line)
#        if n_received:
#            print ip + ": " + status[int(n_received[0])]
class ip_check(threading.Thread):
   def __init__ (self,ip):
      threading.Thread.__init__(self)
      self.ip = ip
      self.__successful_pings = -1
   def run(self):
      ping_out = os.popen("ping -q -c2 "+self.ip,"r")
      while True:
        line = ping_out.readline()
        if not line: break
        n_received = re.findall(received_packages,line)
        if n_received:
           self.__successful_pings = int(n_received[0])
   def status(self):
      if self.__successful_pings == 0:
         return "no response"
      elif self.__successful_pings == 1:
         return "alive, but 50 % package loss"
      elif self.__successful_pings == 2:
         return "alive"
      else:
         return "shouldn't occur"
received_packages = re.compile(r"(\d) received")

check_results = []
for suffix in range(1,10):
   ip = "10.0.2."+str(suffix)
   current = ip_check(ip)
   check_results.append(current)
   current.start()

for el in check_results:
   el.join()
   print "Status from ", el.ip,"is",el.status()

