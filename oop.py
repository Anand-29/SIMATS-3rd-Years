# #encapsulation:
# class Bank:
#     def __init__(self,d):
#         self.__balance=d
#     def credit(self,d):
#         self.__balance+=d
#     def debit(self,d):
#         if d>self.__balance:
#             print("Insufficient balance.")
#         else:
#             self.__balance-=d
#     def get_balance(self):
#         print(self.__balance)
# customer1=Bank(1000)
# customer1.credit(100)
# customer1.debit(500)
# customer1.get_balance()

#Inheritance:
#single inheritance:
# class Animal:
#     def type(self):
#         print("Type Animal")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# d=Dog()
# d.sound()
# d.type()

#Multiple Inheritance:
# class Math:
#     def get_math_marks(self):
#         print(56)
# class Computer:
#     def get_computer_marks(self):
#         print(65)
# class Student(Math,Computer):
#     def __init__(self,name):
#         self.name=name
# s1=Student("Anand")
# s1.get_math_marks()
# s1.get_computer_marks()

#multi level:
# class College:
#     def get_college_name(self):
#         print("SIMATS")
# class Department(College):
#     def get_department(self):
#         print("Medical coding")
# class Section(Department):
#     def get_section(self):
#         print("Section A")
# class Student(Section):
#     def __init__(self,name):
#         self.name=name
# student1=Student("Anand")
# print(student1.name)
# student1.get_section()
# student1.get_department()
# student1.get_college_name()

#hierarchical inheritance:
# class Country:
#     def get_country(self):
#         print("India")
# class Largest_state(Country):
#     def get_largest_state(self):
#         print("Rajasthan")
# class Capital(Country):
#     def get_capital(self):
#         print("Delhi")
# class Smallest_state(Country):
#     def get_smallest_state(self):
#         print("Goa")
# c=Largest_state()
# c.get_country()
# c.get_largest_state()

#hybrid inheritance:
# class A:
#     def get_class_A(self):
#         print("Class-A")
# class B:
#     def get_class_B(self):
#         print("Class-B")
# class C(B,A):
#     def get_class_C(self):
#         print("Class-C")
# class D(C):
#     def get_class_D(self):
#         print("Class-D")
# c=C()
# c.get_class_A()
# c.get_class_B()

#polymorphism:
#method overriding:
# class Animal:
#     def sound(self):
#         print("Animal sound")
# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog sound")
# d=Dog()
# d.sound()

#over loading:
# class Overload:
#     def add(self,x,y,z=0,i=0):
#         print(x+y+z+i)
# ob=Overload()
# ob.add(4,5)
# ob.add(2,3,4)
# ob.add(1,2,3,4)

# #Abstraction:
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         print(self.l*self.b)
# r=Rectangle(4,6)
# r.area()    

#special or duner methods:
# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+other.y)
#     def __str__(self):
#         return f"{self.x},{self.y}"
# v1=Vector(3,4)
# v2=Vector(4,5)
# print(v1+v2)

#Banking System:
# class Account:
#     def __init__(self,acc_no,holder,balance=0):
#         self.acc_no=acc_no
#         self.holder=holder
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         if self.__balance<amount:
#             print("Insufficient balance.")
#         else:
#             self.__balance-=amount
#     def get_balance(self):
#         return self.__balance
# class SavingsAccount(Account):
#     def __init__(self,ac_no,holder,bal=0,intrest=0.10):
#         super().__init__(ac_no,holder,bal)
#         self.intrest=intrest
#     def add_intrest(self):
#         ins=self.get_balance()*self.intrest
#         self.deposit(ins)
# customer1=SavingsAccount(1001,"Anand",1000)
# customer1.withdraw(500)
# print(f"customer1 ac_no: {customer1.acc_no}")
# print(f"customer1 name: {customer1.holder}")
# print(f"Balance: {customer1.get_balance()}")













































        
        
        
        
        
        
        
        
        






