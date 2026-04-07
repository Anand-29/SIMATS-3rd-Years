# #handle ZeroDivisionError:
# try:
#     x=int(input("Enter numerator: "))
#     y=int(input("Enter denominator: "))
#     print(x//y)
# except ZeroDivisionError:
#     print(ZeroDivisionError)
#     print("Invalid answer.")

# #handle ValueError:
# try:
#     x=int(input("Enter integer data: "))
# except ValueError:
#     print("Invalid input.")
# else:
#     print(x)

# #else and finally block:
# try:
#     x=int(input("Enter numerator: "))
#     y=int(input("Enter denominator: "))
#     x=x//y
# except ZeroDivisionError:
#     print("Invalid input.")
# else:
#     print(x)
# finally:
#     print("Code complete.")
    
# #handle FileNotFoundError:
# import os
# with open("name.txt","w") as f:
#     f.write("This is a file. ")
# try:
#     with open("name.txt","r") as f:
#         c=f.read()
# except FileNotFoundError:
#     print(FileNotFoundError)
# else:
#     print(c)
# finally:
#     os.remove("name.txt")

# #write user input to file:
# text=input("Enter the message: ")
# with open("file.py","w") as f:
#     f.write(text)
# with open("file.py","r") as f:
#     print(f.readline())
    
# #append data to existing file:
# file_name=input("Enter file name: ")
# file_msg=input("Enter file message: ")
# with open(file_name,'a') as f:
#     f.write('\n'+file_msg)
# with open(file_name,'r') as f:
#     for i in f:
#         print(i,end=" ")

# #check file exists before reading
# import os
# with open("file.txt","w") as f:
#     f.write("Message1 Message2 Message2")

# if os.path.exists("file.txt"):
#     with open("file.txt","r") as f:
#         print(f.read(5))
# else:
#     print("file not found.")

# #custom exception with -ve number:
# class NegativeNumberException(Exception):
#     pass
# try:
#     x=int(input("Enter +ve number: "))
#     if x<0:
#         raise NegativeNumberException("No -ve numbers")
# except NegativeNumberException as e:
#     print(NegativeNumberException)
#     print(e)
# else:
#     print(x)

# #handle multiple exceptions:
# try:
#     x=int(input("Enter data: "))
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except Exception as e:
#     print(e)

# #handle multiple exceptions:
# try:
#     x=int(input("Enter the data: "))
# except (ValueError,ZeroDivisionError) as e:
#     print(e)
    
# #read all lines from a file as list:
# import os
# file_name=input("Enter the file name:")
# file_msg=input("Enter a sentence:").split()
# with open(file_name,"a") as f:
#     for i in file_msg:
#         f.write(i+"\n")
# if os.path.exists(file_name):
#     with open(file_name,"r") as f:
#         data=f.readlines()
# print(data)

# #import math module:
# from math import sqrt,factorial
# print(sqrt(9))
# print(factorial(5))
# print(sum([5,5]))

data='''# #rename a file:
# file_name=input("Enter the file name: ")
# with open(file_name,"w") as f:
#     pass
# import os
# new_name=input("Enter the new name: ")
# if os.path.exists(file_name):
#     os.rename(file_name,new_name)'''
#count no of lines,words n characters for a file:
file_name=input("Enter the file name: ")
with open(file_name,"w") as f:
    f.write(data)
word_count=0;char_count=0;lines_count=0
with open(file_name,"r") as f:
    for i in f:
        lines_count+=1
        print(i.split())
        word_count+=len(i.split())
        for j in i.split():
            char_count+=len(j)
print(f"word_count: {word_count}")
print(f"char_count: {char_count}")
print(f"lines_count: {lines_count}")












