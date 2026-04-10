#OrderedDict:
# from collections import OrderedDict
# dict=OrderedDict()
# n=int(input("Enter the size: "))
# for i in range(n):
#     key=input("Enter key data: ")
#     value=input("Enter value data: ")
#     dict[key]=value
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict)

#binary search:
# li=list(map(int,input("Enter sorted data: ").split()))
# data=int(input("Enter the search data: "))
# low=0;high=len(li)-1
# while low <= high:
#     mid=(low+high)//2
#     if li[mid]==data:
#         print(f"data found at {mid} index.")
#         break
#     elif data<li[mid]:
#         high=mid-1
#     elif data>li[mid]:
#         low=mid+1
# if low>high:
#     print("Data not found.")

#Binary Search(recursive):
# def binary(li,l,h,data):
#     while l<=h:
#         mid=(l+h)//2
#         if data==li[mid]:
#             return f"data found at index {mid}"
#         elif data<li[mid]:
#             return binary(li,l,mid-1,data)
#         elif data>li[mid]:
#             return binary(li,mid+1,h,data)
#     return "Data not found"
# li=list(map(int,input("Enter the data: ").split()))
# print(binary(li,0,len(li)-1,int(input("Enter search :"))))

#write a progrma to add any no. of parameters:
# def add(*args):
#     return sum(args)
# print(f"Sum: {add(2,3)}")
# print(f"Sum: {add(2,3,5)}")
# print(f"Sum: {add(2,3,8,2)}")
# print(f"Sum: {add(2,3,4,2,9)}")

#set n get student marks using Encapsulation:
# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.__marks=0
#     def set_marks(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
# student1=Student(input("Enter student1 name: "))
# print(student1.name)
# student1.set_marks(int(input("Enter marks: ")))
# print(student1.get_marks())
        
#calculate salary using Abstraction:
# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self,performance,leaves):
#         pass
# class Manager(Employee):
#     def __init__(self,emp_name,lpa):
#         self.emp_name=emp_name
#         self.lpa=lpa*100000
#     def calculate_salary(self,performance,leaves):
#         salary_permonth=(self.lpa/12)
#         pf=(salary_permonth/100)*7
#         insurance=500
#         tax=(salary_permonth/100)*5
#         performance=(5-performance) * 500
#         leaves*=(salary_permonth/30)
#         deductions=pf+tax+leaves+insurance+performance
#         sal=salary_permonth - deductions
#         return f"Salary: ₹ {sal}"
# emp1=Manager("Anand",4)
# salary=emp1.calculate_salary(5,0)
# print(salary)
        
#method overiding: display all the methods:
# class Bus:
#     def display(self):
#         print("Bus-6 wheels")
# class Car:
#     def display(self):
#         print("Car-4 wheels")
# class Bike:
#     def display(self):
#         print("Bike-2 wheels")
# v=[Bus(),Car(),Bike()]
# for i in v:
#     i.display()















