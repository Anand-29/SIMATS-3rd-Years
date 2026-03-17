#Singly Linked List:
class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            t=self.head
            while t.next is not None:
                t=t=t.next
            t.next=newnode
    def display(self):
        t=self.head
        while t is not None:
            print(t.data,end=" -> ")
            t=t.next
        print(t)
    def insert_front(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_pos(self,data,pos):
        newnode=Node(data)
        t=self.data
        while pos > 1 :
            t=t.next
            pos-=1
        newnode.next=t.next
        t.next=newnode
    def delete_front(self):
        self.head=self.head.next
    def delete_end(self):
        t=self.head
        while t.next.next is not None:
            t=t.next
        t.next=None
    def delete_pos(self,pos):
        t=self.head
        while pos > 1 :
            t=t.next
            pos-=1
        t.next=t.next.next
ob=LinkedList()
while True:
    print("Enter 1 to insert data at end: ")
    print("Enter 2 to insert data at front: ")
    print("Enter 3 to enter the data at a position: ")
    print("Enter 4 to delete front: ")
    print("Enter 5 to delete end: ")
    print("Enter 6 to delete pos: ")
    print("Enter 7 to display List: ")
    print("Enter 8 to exit: ")
    c=int(input())
    if c==1:
        a=int(input("Enter the input data: "))
        ob.insert_end(a)
        print("Data inserted at end : ")
    elif c==2:
        a=int(input("Enter the input data: "))
        ob.insert_front(a)
        print("Data inserted at front: ")
    elif c==3:
        a=int(input("Enter the input data: "))
        pos=int(input("Enter the pos: "))
        ob.insert_pos(a,pos)
        print("Data inserted at position: ")
    elif c==4:
        ob.delete_front()
        print("Data deleted at front: ")
    elif c==5:
        ob.delete_end()
        print("Data deleted at end: ")
    elif c==6:
        pos=int(input("Enter the position to be deleted: "))
        ob.delete_pos(pos)
        print("Data deleted at position: ")
    elif c==7:
        print("LinkedList: ")
        ob.display()
    else:
        break
    
    
    
    
    
    
    
    
    









