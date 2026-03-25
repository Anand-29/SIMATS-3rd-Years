#Find nth node from first and last in a SLL:
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
    def length(self):
        t=self.head
        c=0
        while t is not None:
            t=t.next
            c+=1
        return c
    def nth_node_from_start(self,n):
        if n<1 or n>self.length():
            return -1
        if n==1:
            return self.head.data
        t=self.head
        while n>1:
            t=t.next
            n-=1
        return t.data
    def nth_node_from_end(self,n):
        n=(self.length()-n)+1
        r=self.nth_node_from_start(n)
        return r
ob=SLL()
data=list(map(int,input("Enter the data : ").split()))
for i in data:
    ob.insert_end(i)
n=int(input("Enter the nth position from start : "))
m=int(input("Enter the nth position from end : "))
start=ob.nth_node_from_start(n)
end=ob.nth_node_from_end(m)
print(f"{n} data from the start is : {start}")
print(f"{m} data from the end is : {end}")













#Detect loop in a SLL:
#Merge 2 sorted SLL into one sorted list:
#Find merge point of two lists:
