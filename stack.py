class node:
    def __init__(self,data):
      self.data=data
      self.next=None
class stack:
    def __init__(self):
       self.head=None

    def isempty(self):
       if self.head==None:
          return True
       else:
          return False
       
    def push(self,data):
       if self.head==None:
          self.head=node(data)
       else:
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
       if self.head==None:
          return 'stack is empty'
       else:
          curr=self.head
          self.head= self.head.next
          curr=curr.next
    def peek(self):
       if self.head==None:
          return 'stack is empty'
       else:
          curr=self.head
          return self.head.data

    def display(self):
       curr=self.head
       if self.isempty():
        return " stack underflow"
       else:
          while curr is not None:
             print(curr.data,end=" ")
             curr=curr.next
             if curr != None:
                print('->',end='')
          return 

if __name__=="__main__":
   mystack=stack()

   mystack.push(4)
   mystack.push(5)
   mystack.push(7)
   mystack.push(77)
   mystack.display()
   mystack.pop()
   mystack.pop()
   print("\nafter performing pop operation : ")
   mystack.display()
   mystack.peek()
   print("\ntop value is:",mystack.peek())
   

