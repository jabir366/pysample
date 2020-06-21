#!/usr/bin/python3
class Node:
    def __init__(self,char):
        self.data =char
        self.next= None

    def get_all(self):
        curr = self
        while curr is not None:
            print(curr.data,'->',end='')
            curr = curr.next
    def insert_char(self,char):
        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(char)
        #print(f"node {curr.next} is added with element {curr.next.data}")
    def set_char(self,char):
        self.data = char
        print(f"data {char} is set")

def make_next(wrd_start,nxt_wrd):
    curr = wrd_start
    while curr is not None:
        if curr.data == ' ':
            curr.next = nxt_wrd
            print(f"made {nxt_wrd.data} as next of word starting with {wrd_start}")
            return
        else :
            curr=curr.next

#def reverse(nodestring):

def make_list(string):
   mynode = Node(string[0]) 
   for i  in string[1:]:
       mynode.insert_char(i)
#   mynode.get_all()
   return mynode

def reverse_list(node):
    start =node
    wrd_start = wrd_end = None
node =make_list("I love geeks for geeks")
#make_next(node.next.next,node.next.next.next)
node.get_all()

#mynode = Node('a')
#mynode.insert_char('b')
#mynode.insert_char('c')
#mynode.get_all()

