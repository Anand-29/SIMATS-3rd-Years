#Doubly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        newnode=Node(data)
        if self.head is None :
            self.head=newnode
        else:
            t=self.head
            while t.next is not None:
                t=t.next
            t.next=newnode
            newnode.prev=t
    def insert_begining(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
    def insert_position(self,data,ind):
        newnode=Node(data)
        if ind == 0:
            self.insert_begining(data)
        else:
            t=self.head
            while ind>1:
                t=t.next
                if t is None:
                    print("Index is not present")
                    return
                ind-=1
            if t.next is None:
                self.insert_end(data)
            else:
                newnode.next=t.next
                newnode.prev=t
                nn.next.prev=newnode
                t.next=newnode
    def delete_front(self):
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        t=self.head
        while t.next is not None:
            t=t.next
        t.prev.next=None
    def delete_pos(self,ind):
        if ind==0:
            self.delete_front()
        t=self.head
        while ind>0:
            t=t.next
            if t is None:
                print("Index not present")
                return
            ind-=1
        if t.next is None:
            self.delete_end()
        t.next.prev=t.prev
        t.prev.next=t.next
    def display_forward(self):
        t=self.head
        while t is not None:
            print(t.data,end=" -> ")
            t=t.next
        print(t)
    def display_backward(self):
        t=self.head
        while t.next is not None:
            t=t.next
        while t is not None:
            print(t.data,end=" -> ")
            t=t.prev
        print(t)
ob=DLL()
while True:
    print("1 @ insert_begining")
    print("2 @ insert_end")
    print("3 @ insert_position")
    print("4 @ delete_front")
    print("5 @ delete_end")
    print("6 @ delete_pos")
    print("7 @ display_forward")
    print("8 @ display_backward")
    print("9 @ exit")
    ch=int(input("Enter no. : "))
    if ch==1:
        ob.insert_begining(int(input("Enter data: ")))
    elif ch==2:
        ob.insert_end(int(input("Enter data: ")))
    elif ch==3:
        a=int(input("Enter data: "))
        ind=int(input("Enter index: "))
        ob.insert_position(a,ind)
    elif ch==4:
        ob.delete_front()
    elif ch==5:
        ob.delete_end()
    elif ch==6:
        ob.delete_pos(int(input("Enter the Index: ")))
    elif ch==7:
        ob.display_forward()
    elif ch==8:
        ob.display_backward()
    else:
        break

