'''
#Factorial 
def fact(n):
    if n<=1:
        return n
    return n*fact(n-1)
n=int(input("Enter n value: "))
print("Factoiial of",n,"is",fact(n))
'''
'''
#Print nos from 1-n 
def numbers_backwards(n):
    if n==0:
        return
    print(n,end="")
    numbers_backwards(n-1)
def numbers_forward(n):
    if n>=1:
        numbers_forward(n-1)
        print(n,end="")
n=int(input("Enter n value: "))
print("Nos from 1 to",n,"is")
numbers_forward(n)
print("\nNos from",n,"to 1 is")
numbers_backwards(n)
'''
'''
#Fibonacci series
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("Enter n value: "))
print("Fibonacci from 1 to",n,"is:")
for i in range(n+1):
    print(fib(i),end=" ")
'''
'''
#sum of n natural nos
def sum(n):
    if n==0:
        return n
    return n+sum(n-1)
n=int(input("Enter n value: "))
print("Sum of",n,"is",sum(n))
'''
'''
#pallindrome check
def pallindrome(n):
    if len(n)<=1:
        return True
    if n[0]!=n[-1]:
        return False
    return pallindrome(n[1:-1])
n=input("Enter string: ")
print("pallindrome" if pallindrome(n) else "Not pallindrome")
'''
'''
#reverse a string 
def rev(s,d):
    if len(s)==0:
        return d
    d+=s[-1]
    return rev(s[:-1],d)
s=input("Enter the String: ")
d=""
print("Reversed: ",rev(s,d))
'''

'''
#Types of function calls:
#1.Without parameters & without return type
def add():
    a,b=5,5
    print(a+b)
add()
#2.Without parameters & with return type
def add():
    a,b=5,5
    return a+b
print(add())
#3.With parameters & without return type
def add(a,b):
    print(a+b)
add(5,10)
#4.With parameters & with return type
def add(a,b):
    return a+b
print(add(5,10))
'''
'''
