
#Bubble sort:
n=int(input("Enter the size: "))
li=list(map(int,input("Enter the data: ").split()))
flag=False
c=0
for i in range(n-1):
    flag=False
    for j in range(n-1-i):
        c+=1
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            flag=True
    print("Data after",i+1,"pass:",li)
    if flag is False:
        break
print(li)
print(c)











