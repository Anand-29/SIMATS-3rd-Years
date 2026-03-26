#Merge point of 2 linked list:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.h1=self.h2=None
    def insert_end(self,head,data):
        newnode=Node(data)
        if head is None:
            return newnode
        else:
            t=head
            while t.next is not None:
                t=t.next
            t.next=newnode
            return head
    def create_merge_point(self,h1,h2):
        t=h2
        while t.next is not None:
            t=t.next
        t.next=h1.next
        return [h1,h2]
    def find_merge_point(self,h1,h2):
        slow=fast=t=h1
        while t.next is not None:
            t=t.next
        t.next=h2
        while fast.next is not None and slow is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return slow.data
        return -1
ob=linked_list()
l1=list(map(int,input("Enter the l1 data: ").split()))
l2=list(map(int,input("Enter the l2 data: ").split()))
for i in l1:
    ob.h1=ob.insert_end(ob.h1,i)
for j in l2:
    ob.h2=ob.insert_end(ob.h2,j)
ob.h1,ob.h2=ob.create_merge_point(ob.h1,ob.h2)
ans=ob.find_merge_point(ob.h1,ob.h2)
if ans>=0:
    print("Merge point is :",ans)
else:
    print("No merge point")
