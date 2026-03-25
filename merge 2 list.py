#Merge 2 sorted SLL into one sorted list:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head1=self.head2=self.head3=None
    def insert_end(self,data,head):
        newnode=Node(data)
        if head is None:
            return newnode
        else:
            t=head
            while t.next is not None:
                t=t.next
            t.next=newnode
            return head
    def display(self,head):
        while head is not None:
            print(head.data,end="->")
            head=head.next
        print(head)
    def merge(self,h1,h2,h3):
        while h1 is not None and h2 is not None:
            if h1.data<h2.data:
                h3=self.insert_end(h1.data,h3)
                h1=h1.next
            else:
                h3=self.insert_end(h2.data,h3)
                h2=h2.next
        while h1 is not None:
            h3=self.insert_end(h1.data,h3)
            h1=h1.next
        while h2 is not None:
            h3=self.insert_end(h2.data,h3)
            h2=h2.next
        return h3
ob=SLL()
data=list(map(int,input("Enter 1 list data: ").split()))
for i in data:
    ob.head1=ob.insert_end(i,ob.head1)
data=list(map(int,input("Enter 2 list data: ").split()))
for i in data:
    ob.head2=ob.insert_end(i,ob.head2)
ob.display(ob.head1)
ob.display(ob.head2)
print("after merge:")
ob.head3=ob.merge(ob.head1,ob.head2,ob.head3)
ob.display(ob.head3)











#Find merge point of two lists:
