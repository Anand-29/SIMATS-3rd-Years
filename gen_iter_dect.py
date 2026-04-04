# class Number:
#     def __iter__(self):
#         self.n=10
#         return self
#     def __next__(self):
#         if self.n<=3:
#             x=self.n
#             self.n+=1
#             return x
#         else:
#             raise StopIteration
# ob=Number()
# for i in ob:
#     print(i)
    
# # itr=iter([1,2,3])
# # print(next(itr))
# # print(next(itr))
# # print(next(itr))

#generator
# def gen():
#     yield 1
#     yield 2
#     yield 3
# ob=gen()
# print(gen)
# print(type(ob))

# gen=(x for x in range(5))
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(list(gen))
# print(list(gen))
# print(next(gen))

#Counter
# from collections import Counter
# li=[1,1,3,2,5,5]
# print(Counter(li))

#print using iter:
# li=[1,2,3,4]
# li=iter(li)
# print(next(li))
# print(next(li))
# print(next(li))

#handle StopIteration
# class Iter:
#     def __init__(self,n):
#         self.curr=0
#         self.end=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.curr<self.end:
#             x=self.curr
#             self.curr+=1
#             return x
#         else:
#             raise StopIteration
# ob=Iter(3)
# print(next(ob))
# print(list(ob))

#Generate a iterator from 1 to 10:
# class Iter:
#     def __init__(self,n):
#         self.curr=1
#         self.end=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.curr<=self.end:
#             x=self.curr
#             self.curr+=1
#             return x
#         else:
#             raise StopIteration
# ob=Iter(10)
# print(list(ob))

#Generate infinite itertor:
# class Iter:
#     def __init__(self):
#         self.n=1
#     def __iter__(self):
#         self.c=1
#         return self
#     def __next__(self):
#         while True:
#             x=self.c
#             self.c+=1
#             return x
# ob=Iter()
# for i in ob:
#     print(i)

#generator for even number:
# def num():
#     even=0
#     while True:
#         if even%2==0:
#             yield even
#         even+=1
# gen=num()
# print(next(gen))
# print(next(gen))
# print(next(gen))

#generator for fibonacci series:
# def fib():
#     a=0
#     b=1
#     print(a)
#     while True:
#         yield b
#         a,b=b,a+b
# gen=fib()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#genetare cube of 1-N numbers
# n=int(input("Enter the Size: "))
# gen=(x**3 for x in range(n))
# print(next(gen))
# print(next(gen))
# print(list(gen))

#compare memory list vs generator:
# import sys
# li=[x for x in range(5000)]
# gen=(x for x in range(5000))
# a=5
# print(sys.getsizeof(li),"bytes")
# print(sys.getsizeof(gen),"bytes")
# print(sys.getsizeof(a),"bytes")

#custom iterator for even numbers:
# class num:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n%2==1:
#             self.n+=1
#         x=self.n
#         self.n+=2
#         return x
# n=int(input("Enter the start data: "))
# itr=num(n)
# print(next(itr))
# print(next(itr))
# print(next(itr))

#Reverse list elements:
# class Iter:
#     def __init__(self,li):
#         self.li=li
#         self.ind=len(li)-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.ind>=0:
#             x=self.li[self.ind]
#             self.ind-=1
#             return x
#         else:
#             raise StopIteration
# num=[1,2,3,4,5]
# ob=Iter(num)
# print(list(Iter(num)))

#Prime numbers using Iterators:
# class Prime():
#     def __init__(self):
#         self.n=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while True:
#             if self.n<=2:
#                 x=self.n
#                 self.n+=1
#                 return x
#             elif self.is_prime(self.n):
#                 x=self.n
#                 self.n+=1
#                 return x
#             self.n+=1
#     def is_prime(self,n):
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
# prime=Prime()
# print(next(prime))
# print(next(prime))
# print(next(prime))
# print(next(prime))

#Iterators with stepsize:
# class Step:
#     def __init__(self,n,s):
#         self.start=n
#         self.step=s
#     def __iter__(self):
#         return self
#     def __next__(self):
#         x=self.start
#         self.start+=self.step
#         return x
# n=int(input("Enter the start data: "))
# s=int(input("Enter the step Size: "))
# step=Step(n,s)
# print(next(step))
# print(next(step))
# print(next(step))

#Generate factorials:
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#       f*=i
#     return f
# def facts(n):
#     c=1
#     while c<=n:
#         yield fact(c)
#         c+=1
# n=int(input("Enter n value: "))
# for i in facts(n):
#     print(i,end=" ")

#Generate pallindrome numbers:
# def pallindrome(n):
#     n=str(n)
#     return n==n[::-1]
# def pallindromes(n):
#     c=1
#     while c<=n:
#         if pallindrome(c):
#             yield c
#         c+=1
# n=int(input("Enter n value: "))
# for i in pallindromes(n):
#     print(i,end=" ")

#Flatten nested list:
# def flatten(li):
#     for i in li:
#         if isinstance(i,list):
#             yield from flatten(i)
#         else:
#             yield i
# li=[1,[2,[3,4],5],6]
# print(list(flatten(li)))

#custom range generator:
# def Range(start,end=None,jump=1):
#     if end is None:
#         end=start
#         start=0
#     while start<end:
#         yield start
#         start+=jump

# for i in Range(5):
#     print(i,end=" ")
# print()
# for i in Range(2,10,3):
#     print(i,end=" ")

#Generator pipeline:
n=int(input("Enter n value: "))
nums=(x for x in range(n))
even=(x for x in nums if x%2==0)
square=(x*x for x in even)
for x in square:
    print(x,end=" ")












































































    

















