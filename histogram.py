#Largest area in histogram:
hist=[int(x) for x in input("Enter the data: ").split()]
left=[]
right=[]
area=[]
c=0
l=len(hist)
for i in range(l):
    c=0
    for j in range(i+1,l):
        if hist[j]>hist[i]:
            c+=1
        else:
            break
    right.append(c)
    c=0
    for k in range(i-1,-1,-1):
        if hist[k]>hist[i]:
            c+=1
        else:
            break
    left.append(c)
for i in range(l):
    area.append(hist[i]*(left[i]+1+right[i]))
print("Left area is : ",left)
print("Right area is : ",right)
print("Each area is : ",area)
print("Largest area is : ",max(area))


