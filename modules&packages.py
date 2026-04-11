#create a module math_ops and create add() and sub():
# import math_ops
# x,y=map(int,input("Enter two data: ").split())
# print(f"Sum: {math_ops.add(x,y)}")
# print(f"Difference: {math_ops.sub(x,y)}")

#create a module file_ops write/read:
# with open("file_ops.py","w"):
#     pass
# from file_ops import write,read
# file_name=input("Enter the file_name: ")
# message=input("Enter the message: ")
# write(file_name,message)
# print(read(file_name))

#list all installed packages
# import subprocess
# result = subprocess.run(["pip", "list"], 
# capture_output=True, text=True)
# print(result.stdout)

#iterator- print nos 1 to N
# class Iterator:
#     def __init__(self,n):
#         self.start=1
#         self.end=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start<=self.end:
#             temp=self.start
#             self.start+=1
#             return temp
#         else:
#             raise StopIteration("No data left.")
# iter=Iterator(5)
# print(next(iter));print(next(iter))
# print(next(iter));print(next(iter))
# print(next(iter));print(next(iter))

#Generator- print squares if nos.
# def square():
#     i=1
#     while True:
#         yield i*i
#         i+=1
# s=square()
# print(next(s))
# print(next(s))

#generate expression for cubes:
# n=input("Enter N value: ")
# gen=(x**3 for x in range(int(n)))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#add two numbers using lambda:
# x,y=map(int,input("Enter two numbers: ").split())
# add=lambda a,b: a+b
# print(add(x,y))

#square numbers using labda and map:
# numbers=list(map(int,input("Enter numbers: ").split()))
# print(f"Before squaring: {numbers}")
# numbers=list(map(lambda x:x**2,numbers))
# print(f"After squaring: {numbers}")

#filer even numbers using lambda and filter:
# numbers=list(map(int,input("Enter numbers: ").split()))
# print(f"Before filtering: {numbers}")
# numbers=list(filter(lambda x:x%2==0,numbers))
# print(f"After filtering : {numbers} <- even numbers")

#reduce numbers using lambda and reduce:
# from functools import reduce 
# numbers=list(map(int,input("Enter numbers: ").split()))
# print(f"Before reducing: {numbers}")
# numbers=reduce(lambda x,y:x*y,numbers)
# print(f"After reducing : {numbers} <- product")

# #list comprehension:
# even_squares=[x**2 for x in range(1,20) if x%2==0]
# print(f"even_squares: {even_squares}")

# print("Multiplication table 1 to 3:")
# mul_table=[[i*j for i in range(1,4)]for j in range(1,10)]
# for row in mul_table:
#     print(row)

# #factorial:
# import math
# print("Factorial:",math.factorial(int(input("Number: "))))

#pyhton env path
# import sys
# print(sys.executable)

#sort list of tuples by second value:
list=[(4,5),(2,7),(1,4),(8,2)]
list.sort(key=lambda x:x[0])
print(f"Sorted based on 1st index: {list}")
list.sort(key=lambda x:x[1])
print(f"Sorted based on 2nd index: {list}")































