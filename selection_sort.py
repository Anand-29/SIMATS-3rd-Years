#Selection sort:
n=int(input("Enter the size: "))
li=list(map(int,input("Enter the data: ").split()))
c=0
for i in range(n-1):
    flag=False
    min=i
    for j in range(i+1,n):
        c+=1
        if li[j]<li[min]:
            min=j
            flag=True
    li[min],li[i]=li[i],li[min]
    print("After",i+1,"pass: ",li)
    if flag is False:
        break
print("sorted list: ",li);print("Count: ",c)
