'''
#Accessing first and last character
s=input("Enter the String : ")
print(f"First character is {s[0]} , the last character is {s[-1]}")
'''

'''
#Extract a substring:
s=input("Enter the String : ")
start_ind=int(input("Enter the start index: "))
end_ind=int(input("Enter the end index: "))
print(f"The substring is : {s[start_ind : end_ind+1]}")
'''

'''
#Count occurance of a character:
s=input("Enter the String : ")
char=input("Enter the char : ")
print(f"The char {char} occurs {s.count(char)} times.")
'''

'''
#Count occurance of a character:
s=input("Enter the String : ")
word=input("Enter the word : ")
print(f"The word {word} occurs {s.count(word)} times.")
'''

'''
#Count number of spcaes in a String:
s=input("Enter the String : ")
print(f"The number of Spaces are {s.count(" ")}.")
'''

'''
#Convert title case without title()
s=input("Enter the String: ").split()
t=""
for i in s:
    s1=str(i)
    s1=s1[0].upper()+s1[1:].lower()+" "
    t+=s1
t=t.rstrip()
print(f"The title case is: {t}")
'''

'''
#convert title case using loops:
s=input("Enter the string : ")
t=""
t+=s[0].upper()
i=1
while(i<len(s)-1):
    if s[i]==" ":
        t+=s[i]
        t+=s[i+1].upper()
        i+=2
    else:
        t+=s[i].lower()
        i+=1
t+=s[len(s)-1]
print(f"The title case is : {t}")
'''

'''
#Remove duplicate preserving order:
x=input("Enter a string : ")
print(set(x)) #->SET: Cannot contain duplicat,unordered
s=""
for i in x:
    if i not in s:
        s+=i
    else:
        pass
print(f"String with distinct data : {s}")
'''

'''
#Print duplicate preserving order:
x=input("Enter a string : ")
print(set(x)) #->SET: Cannot contain duplicat,unordered
s=""
ans=""
for i in x:
    if i not in s:
        s+=i
    else:
        if i not in ans:
            ans+=i
print(f"Duplicate values in string : {ans}")
'''

'''
#Check two string are anagram(sort based):
def check_anangram(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        return True
    return False
    
s1=input("Enter the String 1 : ")
s2=input("Enter the String 2 : ")
ans=check_anangram(s1,s2)
print("The string are anagram" if ans==True else "The strings are not anangram")
'''

'''
#Check two Strings are anagram(Frequency Based):
def check_anangram(s1,s2):
    if len(s1) != len(s2):
        return False
    freq=[x*0 for x in range(26)]
    for i in s1:
        ind=ord(i)-97 # uppercase ascii -> 65
        freq[ind]+=1
    for i in s2:
        ind=ord(i)-97
        freq[ind]-=1
    for i in freq:
        if i!=0:
            return False
    return True

s1=input("Enter the String 1 : ").lower()
s2=input("Enter the String 2 : ").lower()
ans=check_anangram(s1,s2)
print("The string are anagram" if ans==True else "The strings are not anangram")
'''

'''
#find maximum word in a String:
s=input("Enter the String: ").split()
max=0
char=""
for i in s:
    t=str(i)
    if len(t)>max:
        max=len(t)
        char=i
print(f"The max character is '{char}' with the length of {max}")
'''

'''
#Remove nth index
s=input("Enter the String: ")
ind=int(input("Enter the index : "))
print(f"String after removing {ind} is {s[:ind]+s[ind+1:]}")
'''

'''
#replace every space with hypen:
s=input("Enter the string: ").replace(" ","-")
print(s)
'''

'''
#largest of 2 word without lne():
s1=input("Enter the string 1: ")
s2=input("Enter the string 2: ")
c1,c2=0,0
for i in s1:
    c1+=1
for i in s2:
    c2+=1
print("String 1 is largest" if c1>c2 else "String 2 is largest")
'''

'''
#form a new string from first and last 2 characters from a string:
s=input("Enter the String: ")
print(f"new string : {s[:2]+s[len(s)-2:]}")
'''

'''
#Characters in ascending order:
x=sorted(input("Enter the string : ").lower().replace(" ",""))
print(f"Ascending order: {''.join(x)}")
'''

'''
#concatinate a substring in a given string:
s=input("Enter the string : ")
sub=input(" Enter the substring : ")
ind=int(input("Enter the index data : "))
print(f"The concatinated string is : {s[:ind+1] + sub + s[ind:]}")
'''

'''
#replace str 1 with str 2:
s1=input("Enter the string 1 : ")
s2=input("Enter the string 2 : ")
if s1.index(s2[0])>-1:
    ind=s1.index(s2[0])
    print(f"The new string is : {s1[:ind]+s2}")
'''

'''
#highest occurance of Character:
s=input("Enter the String: ")
dummy=set(s)
max=0
char=""
for i in dummy:
    ans=s.count(i)
    if ans>max:
        max=ans
        char=i
print(f"{char} : {max}")
'''










































    
    
    
    
    
    
    




























