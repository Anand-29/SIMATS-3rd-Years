#square numbers
num=[1,2,3,4]
print([x**2 for x in num])

#even numbers:1-20
print([x for x in range(20) if x%2==0])

#dictonary of cube:
print({x:x**3 for x in range(5)})

#remove vowels form string:
print([x for x in "anand" if x not in "aeiou"])

#flatten list
num=[[1,2],[3,4]]
print([num[i][j] for i in range(len(num)) for j in range(len(num))])

#even -> 0 , odd -> numbers
print([0 if x%2==0 else x for x in range(20)])

#set of unique squares
li=[1,2,2,3,3]
print({x**2 for x in li})

#multiplication table
print([x*y for x in range(1,3) for y in range(1,10)])

#filter string where len>3:
str=["abcd","ab","abcdef"]
print([x for x in str if len(x)>3])

#dictonary form 2 lists
keys=[1,2,3,4]
val=[10,20,30,40]
print({keys[x]:val[x] for x in range(len(keys))})

#find square of odd numbers
li=[1,2,3,4,5]
print([x**2 if x%2==1 else x for x in li])

#convert list ro dictonary
li=[1,2,3,4]
print({ind:li[ind] for ind in range(len(li))})

#extract vowels from string:
str="programming"
print([x for x in str if x in "aeiou"])

#create a list of tuples
li=[1,2,3,4]
print([(i,li[i]) for i in range(len(li))])

#remove duplicate
print(set([1,22,3,3,4,4]))

#flatten 2d list n filter odd numbers
num=[[1,2],[3,4]]
print([num[i][j] for i in range(len(num)) for j in \
range(len(num)) if num[i][j]%2==1])

#dict of square: cube
print({ x**2 :x**3 for x in range(5)})

#replace -ve num with 0
li=[1,-3,5,-2]
print([0 if x<0 else x for x in li])

#frequency
s="aabbbcccd"
print({x:s.count(x) for x in set(s)})




