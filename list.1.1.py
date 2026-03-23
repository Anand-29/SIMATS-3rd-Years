'''
#Find max and min:
n=int(input("Enter the size of list: "))
li=[]
for i in range(n):
    a=int(input(f"Enter {i} data: "))
    li.append(a)
min=max=li[0]
for i in range(1,n):
    if li[i]>max:
        max=li[i]
for i in range(1,n):
    if li[i]<min:
        min=li[i]
print(f"The max is : {max} , min is : {min}")
'''

'''
#Reverse using 2 pointers:
li=list(map(int,input("Enter the data: ").split()))
i,j=0,len(li)-1
while i != j :
    li[i],li[j]=li[j],li[i]
    i+=1
    j-=1
print(li)
'''

'''
#Move all 0's to end:
li=list(map(int,input("Enter the data: ").split()))
i,j=0,len(li)-1
while i < j :
    if li[i]==0:
        li[i],li[j]=li[j],li[i]
        i+=1
    if li[j]!=0:
        li[i],li[j]=li[j],li[i]
        j-=1
    else:
        i+=1
        j-=1
print(li)
'''

'''
#Move all 0's to end(same order):
li=list(map(int,input("Enter the data: ").split()))
ind=0
for i in range(len(li)):
    if li[i] != 0:
        li[i],li[ind]=li[ind],li[i]
        ind+=1
print(li)
'''

'''
#Rotate list by K positions:
li=list(map(int,input("Enter the data: ").split()))
k=int(input("Enter the K data: "))
sub1=li[0:len(li)-k][::-1]
sub2=li[len(li)-k:len(li)][::-1]
for i in sub2:
    sub1.append(i)
sub1=sub1[::-1]
print(sub1)
'''

'''
#2 sum:
li=list(map(int,input("Enter the data: ").split()))
t=int(input("Enter target sum: "))
li.sort()
i,j=0,len(li)-1
while i<j:
    if li[i]+li[j]>t:
        j-=1
    elif li[i]+li[j]<t:
        i+=1
    else:
        print(li[i],li[j])
        i+=1
        j-=1
'''




















































