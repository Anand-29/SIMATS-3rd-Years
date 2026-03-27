#Insertion sort:
n=int(input("Enter the size: "))
li=list(map(int,input("Enter the data: ").split()))
for i in range(1,n):
    key=li[i]
    j=i-1
    while j>=0 and li[j]>key:
        li[j+1]=li[j]
        j-=1
    li[j+1]=key
    print("List after",i,"pass",li)
print("Sorted list: ",li)
