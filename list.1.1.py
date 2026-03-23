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
'''
#largest subarray sum in an continous array/list:
#Kadane's Algorithm
li=list(map(int,input("Enter the data: ").split()))
csum=lsum=li[0]
for i in range(1,len(li)):
    csum=max(csum+li[i],li[i])
    lsum=max(lsum,csum)
print(f"Largest subarray sum : {lsum}")

9020
9041
9060
'''

'''
#Remove duplicate in an Sorted list:
li=list(map(int,input("Enter the data: ").split()))
ans=[]
for i in li:
    if i not in ans:
        ans.append(i)
print(ans)
'''

'''
#Find second Largest in a List:
li=list(map(int,input("Enter the data: ").split()))
l,sl=li[0],-1
for i in range(1,len(li)):
    if li[i]>l:
        sl=l
        l=li[i]
    if li[i]<l and li[i]>sl:
        sl=li[i]
print(f"Second Largest : {sl}")

print(sorted(li)[-2])
'''

'''
#Squares of even numbers btw 1-20 using comprehension:
x=[i**2 for i in range(1,20+1) if i%2==0]
print(x)
'''

'''
#list of prime nos using list comprehension:
def is_prime(x):
    if x<=2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True
x=[i for i in range(1,100+1) if is_prime(i)]
#y=[i for i in range(1,100+1) if all(i%j!=0 for j in range(2,i))]
print(x)
'''
'''
#Flatten 2D into 1D list:
#method 1
li=[[10,20],
    [30,40]]
ans=[]
for i in range(2):
    for j in range(2):
        ans.append(li[i][j])
print(ans)
#method 2
x=[li[i][j] for i in range(len(li)) for j in range(len(li))]
print(x)
print(li)
'''
'''
#index & value using enumerate():
li=[10,20,30,40]
for i,j in enumerate(li):
    print(f"ind: {i}, val : {j}")
'''

'''
#String sort based on length:
li=["banana","avacado",]
print(f"Alphabetical : {sorted(li)}")
print(f"Based on length: {sorted(li,key=len)}")
'''

























































































































