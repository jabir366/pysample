#!/usr/bin/env python3
import zmq
import time,json
import utilities as util
from threading import Thread
from subprocess import Popen, PIPE
NBR_WORKERS = 5

def ping(ip):
  cmd = f"ping -c1 -q {ip}".split()
  stdout,stderr = util.execute_command(cmd)
  return {'output':stdout}

def worker(worker_url,context =None):
  context = context or zmq.Context.instance()
  socket = context.socket(zmq.REP)
  socket.connect(worker_url)
  while True:
    message =socket.recv().decode()
    print(f"Received request: {message}" )
    op = ping(message)
    time.sleep(.2)
    socket.send(str.encode(json.dumps(op)))

url_worker = "inproc://workers"
url_client = "tcp://*:5553"
context = zmq.Context.instance()
clients = context.socket(zmq.ROUTER)
#server_socket = context.socket(zmq.ROUTER)
#server_socket.bind("tcp://*:5553")
clients.bind(url_client)
workers = context.socket(zmq.DEALER)
workers.bind(url_worker)
for i in range(5):
  thread = Thread(target=worker, args=(url_worker,))
  thread.start()
zmq.proxy(clients, workers)
clients.close()
workers.close()
context.term()


#while True:
#    #  Wait for next request from client
#    #message = socket.recvREP()
#    address, empty, ready = server_socket.recv_multipart()
#    print ("Received request in main: ", ready.decode())
#    op = ping(ready.decode())
#    #  Do some 'work'
#
#    #  Send reply back to client
#    server_socket.send_multipart( [address,empty,str.encode(json.dumps(op))])
#    #socket.send(b"World")
