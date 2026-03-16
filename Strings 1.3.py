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

#Reverse words in a string:
s=' '.join(input("Enter String: ").split()[::-1])
print(f"Reversed string : {s}")






















