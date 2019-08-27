#!/usr/bin/env python3
#   Sends "Hello" to server, expects "World" back
#
import zmq

context = zmq.Context()

#  Socket to talk to server
print ("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:5553")

#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print ("Sending request %", request, "...")
    socket.send (b"123.56.2.3")

    #  Get the reply.
    message = socket.recv()
    print ("Received reply ", request,  message.decode())
