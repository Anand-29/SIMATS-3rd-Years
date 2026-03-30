#2.Binary Search:
def binary_search(li,key):
    if len(li)==0:
        return False
    mid=len(li)//2
    if li[mid]==key:
        return True
    elif key<li[mid]:
        return binary_search(li[:mid],key)
    elif key>li[mid]:
        return binary_search(li[mid+1:],key)
li=[int(x) for x in input("Enter data: ").split()]
li.sort()
key=int(input("Enter the key data: "))
print("Present" if binary_search(li,key) else "Not Present")
