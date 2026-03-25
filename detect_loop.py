#Detect loop in a SLL:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            t=self.head
            while t.next is not None:
                t=t.next
            t.next=newnode
    def create_loop(self):
        t=self.head
        while t.next is not None:
            t=t.next
        t.next=self.head.next.next
    def detect_loop(self):
        slow=self.head
        fast=self.head
        while fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False
ob=SLL()
data=list(map(int,input("Enter the data: ").split()))
for i in data:
    ob.insert_end(i)
ob.create_loop()
print("Loop detected" if ob.detect_loop() else "No loop")














#Merge 2 sorted SLL into one sorted list:
#Find merge point of two lists:
