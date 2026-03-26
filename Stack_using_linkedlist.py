#Stack creation- using linked list and using arr/list:
#Stack operations - push(),pop(),peek(),top(),isempty(),overflow(),underflow()
#Stack process - Last in first out(LIFO)

#Stack using linked list:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        if self.top is None:
            return True
        return False
    def peek(self):
        return self.top.data
    def push(self,data):
        newnode=Node(data)
        if self.isempty():
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.isempty():
            print("Empty stack")
            return
        data=self.top.data
        self.top=self.top.next
        return data
ob=Stack()
while True:
    print("press 1 to push() | 2 to pop() | 3 to peek() | 4 to exit() | ")
    c=int(input())
    if c == 1:
        d=int(input("Enter the data: "))
        ob.push(d)
    elif c==2:
        print(f"{ob.pop()} is deleted")
    elif c==3:
        print(f"Top data is : {ob.peek()}")
    else:
        break
    
    
    
    
    
    
    
