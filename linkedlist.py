class node:
    def __init__(self,value):
        self.data=value
        n=self.next=None
class linkedlist:
  def __init__(self):
    self.head=None
    self.n=0
  def __len__(self):
    return self.n

  #insert value in ll

  def insert_head(self,value):
    new_node=node(value)
    new_node.next=self.head
    self.head=new_node
    self.n=self.n + 1

  def insert_after(self,after,value):
    new_node=node(value)
    curr=self.head
    
    while curr != None:
     if curr.data==after:
      break
    curr=curr.next

    if curr != None:
      new_node.next=curr.next
      curr.next=new_node
      self.n= self.n+1
    else:
      return ' item not found'
 #traverse data and print
  def __str__(self):
    curr=self.head
    result=''
    while curr != None:
     result= result+str(curr.data) + '->'   
     curr=curr.next
    return result[:-2]
 
 #append value
  def append(self,value):
    new_node=node(value)
    #empty list
    if self.head==None:
      self.head==new_node
      self.n= self.n + 1
    #if not
    curr=self.head
    while curr.next != None:
      curr=curr.next
    curr.next=new_node
    self.n=self.n+1
  
  #insert at middle
  
#clear the node
  def clear(self):
    self.head==None
    self.n=0
    return 'node is empty'
#dlt from head
def dlt_head(self):
  if self.head==None:
    return ' empty ll'
  self.head=self.head.next
  self.n= self.n-1

def pop(self):
  if self.head==None:
    return 'empty ll'
  
  curr=self.head
  if curr.next==None:
    return self.dlt_head()
  while curr.next.next != None:
    curr=curr.next
  curr.next=None
  self.n=self.n-1
  
l=linkedlist()
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
l.dlt_head()

print(l)
