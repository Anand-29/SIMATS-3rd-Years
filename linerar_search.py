#1.Linear Search:
def linear_search(li,key):
    for i in range(len(li)):
        if li[i]==key:
            return i
    return -1
n=int(input("Enter the size: "))
li=[int(x) for x in input("Enter data: ").split()]
key=int(input("Enter the key data: "))
ind=linear_search(li,key)
if ind>=0:
    print("The data",key,"is present at index:",ind)
else:
    print("Key not present")
'''
