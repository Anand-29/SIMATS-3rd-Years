#program 1
# import math
# def area(shape,a):
#     if shape=="circle":
#         return f"area of circle : {math.pi*a*a}"
#     else:
#         return f"area of square : {a*a}"
# shape=input("Enter shape: ")
# if shape=="circle":
#     print(area(shape,float(input("Enter radius:"))))
# else:
#     print(area(shape,int(input("Enter length: "))))
    
#Program 2
# class Animal:
#     def sound(self):
#         print("Animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog sound")
# class Cat(Animal):
#     def sound(self):
#         print("Cat sound")
# d=Dog();c=Cat()
# d.sound()
# c.sound()
    
#Program 3   
# from abc import ABC,abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def area(self,a=0,b=0):
#         pass
# class Rectangle(Shape):
#     def area(self,a,b):
#         return f"area of Rectangle: {a*b}"
# class Circle(Shape):
#     def area(self,a,b=0):
#         return f"area of Circle: {math.pi*a*a}"
# r=Rectangle();c=Circle()
# print(r.area(5,10))
# print(c.area(5))

#Implement Deque:
from collections import deque 
dq=deque()
while True:
    print("Enter:")
    print("1 to add data left")
    print("2 to add data right")
    print("3 to delete data left")
    print("4 to delete data right")
    print("5 to display")
    print("6 to exit.")
    c=int(input("Enter the choice: "))
    if c == 1:
        dq.appendleft(int(input("Enter data:")))
    elif c == 2:
        dq.append(int(input("Enter data:")))
    elif c == 3:
        dq.popleft()
    elif c == 4:
        dq.pop()
    elif c == 5:
        print(dq)
    else:
        break










    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
