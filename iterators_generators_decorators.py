#addition using lambda
add=lambda x,y:x+y
print(add(5,10))

#filter even numbers from a list
num=[1,2,3,4,5]
even=list(filter(lambda x : x%2==0,num))
print(even)

#product of list:
from functools import reduce
num=[1,2,3,4,5]
prod=reduce(lambda x,y: x*y,num)
print(prod)

#iterators
num=[1,2,3]
iterobj=iter(num)
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
#print(next(iterobj))

#Generators
def fun(n):
    i=1
    while i<n:
        yield i
        i+=1
gen=fun(5)
for i in gen:
    print(i)

#decorators
#passing a fun as parameter
def fun(s,name):
        name(s)
def name(s):
    print(s)
s="Anand"
fun(s,name)

#returning a function as value:
def fun():
    def add(x,y):
        return x+y
    return add
ans=fun()
print(ans(5,10))





















