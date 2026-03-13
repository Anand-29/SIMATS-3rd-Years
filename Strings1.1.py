'''
#reverse a string:
s=input()[::-1]
print(s)

#or
s=input()
ans=s[::-1]
print(ans)
'''

'''
#count vowels in a string:
count=0
s=input().lower()
for i in s:
    if i in "aeiou":
        count+=1
print(f"Number of vowles present in the string are {count}")
'''

'''
#find length of the string without using string len():
count=0
s=input()
for i in s:
    count+=1
print(f"length of string is {count}")
'''

'''
#count number of upper and lower case in a string:
n=input()
upper,lower=0,0
for i in n:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(f"The number of lowercase is {lower} & number of uppercase is {upper}")
'''

'''
#count number of words in a string:
s=input().split()
print(f"Number of words in the String : {len(s)}")
'''

'''
import string
print(string.ascii_lowercase)
alphabets=string.ascii_lowercase
s=input().lower()
if len(alphabets)<=len(set(s)):
    print("The string is Pangram")
else:
    print("The string is not pangram")
'''


# #Remove all the vowels in a String:
# s=input().lower()
# result=""
# for i in s:
#     if i not in "aeiou":
#         result+=i
# print(f'''String without vowels : "{result}" ''')

'''
#Count number of consonant:
s=input().lower()
count=0
for i in s:
    if i.isalpha():
        if i not in "aeiou":
            count+=1
print(f"Number of consonant in the string is : {count}")
'''

'''
#Reverse a string using Recurssioin:
def reverse_str(s):
    if s=="":
        return ""
    else:
        return reverse_str(s[1:])+s[0]
s=input("Enter the String : ")
ans=reverse_str(s)
print(f"The reversed string is : {ans}")
'''























































































