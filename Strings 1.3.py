'''
#String Encryption
s=input("Enter the string: ")
key=int(input("Enter the key"))
ans=""
for i in s:
    if i==" ":
        ans+=" "
    else:
        if i.islower():
            ascii=ord(i)-97 #ord('a')
            ascii=(ascii+key)%26
            ascii=chr(ascii+97)
            ans+=ascii
        if i.isupper():
            ascii=ord(i)-65 #ord('A')
            ascii=(ascii+key)%26
            ascii=chr(ascii+65)
            ans+=ascii
print(f"The encrypted string is : {ans}")
'''

'''
#Length Encoding:
s=input("Enter the String: ")
di={}
for i in s:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
ans=""
for i in di:
    ans+=i
    ans+=str(di[i])
print(f"Length Encoding : {ans}")
'''

'''
#Frequency of characters:
s=input("Enter the String : ")
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
li=sorted(freq)
for i in li:
    print(f"{i} : {freq[i]}")
'''

'''
#Frequency of words:
s=input("Enter the String : ")
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
'''

'''
#Binary String:
s=input("Enter the String: ")
if set(s)<={'0','1'}:
    print("Binary String")
else:
    print("Not a binary String")
'''

'''
#Check whether the String contains vowels:
s=input("Enter the string: ").lower()
d="aeiou"
t=""
for i in d:
    if i in s:
        t+=i
print("Vaild" if t==d else "Invaild")
'''

'''
#Print missing alphabets:
import string
s=input("Enter the string : ").lower()
s=''.join([x for x in string.ascii_lowercase if x not in s])
print(f"Missing alphabets : {s}")
'''

'''
#Reverse words in a string:
s=' '.join(input("Enter String: ").split()[::-1])
print(f"Reversed string : {s}")
'''

'''
#find substring:
s1=input("Enter the String: ")
s2=input("Enter the search String: ")
print(s1.find(s2))
print("Present" if s1.find(s2)>-1 else "Not Present")
'''

'''
#isomorphic strings:
s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
m1,m2={},{}
flag=True
for c1,c2 in zip(s1,s2):
    if c1 in m1 and m1[c1]!=c2:
        flag=False
        break
    if c2 in m2 and m2[c2]!=c1:
        flag=False
        break
    m1[c1]=c2
    m2[c2]=c1
print("Isomorphic Strings" if flag else "Not Isomorphic Strings")
'''

'''
#Longest non repeating substring:
s=input("Enter the String: ")
map1={}
start=0
maxv=0
ans=""
for i,ch in enumerate(s):
    if ch in map1 and map1[ch]>=start:
        start=map1[ch]+1
    map1[ch]=i
    curr_length=i-start+1
    if curr_length>=maxv:
        maxv=curr_length
        ans=s[start:i+1]   
print(f"Max size is {maxv} and sub-string is {ans}")
'''

#Longest prefix of given string:
s=input("Enter the string: ").split()
pre=s[0]
for i in s[1:]:
    while not i.startswith(pre):
        pre=pre[:-1]
print(f"Longest common prefix : '{pre}'")




























    
















