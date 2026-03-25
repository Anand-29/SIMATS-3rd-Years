#creat a tuple
t=(10,20,30,20)
print(t)
#length
print(len(t))
#access firat n last:
print(t[0],t[-1])
#count occurence of element:
print(t.count(20))
#find index of element:
print(t.index(30))
#Concanate two tuples:
t3=t+(40,50)
print(t3)
#print tuple multiple times:
print(t3*5)
#convert list to tuple:
t4=tuple([10,20,30])
print(type(t4))
#tuple unpacking
a,*b=(10,20,30,40)
print(a);print(b)
#nested tuple:
t5=((1,2),(3,4,5),5,(6,7))
print(t5[0])
print(t5[0][0])
#user input:
t6=tuple(map(int,input().split()))
print(t6)
