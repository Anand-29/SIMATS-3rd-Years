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
    
    
    
    
    
    
    
    
    




























