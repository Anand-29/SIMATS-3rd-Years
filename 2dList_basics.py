#2d matrix:
n=int(input("Enter the data: "))
mat=[[x for x in range(n)] for i in range(n)]
count=1
for i in range(n):
    for j in range(n):
        mat[i][j]=count
        count+=1
#####################################
print("Matrix: ")
for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()
#####################################
print("First row data:")
for i in range(n):
    for j in range(n):
        if i==0:
            print(mat[i][j],end=" ")
    print()
#####################################
print("Second row data:")
for i in range(n):
    for j in range(n):
        if i==1:
            print(mat[i][j],end=" ")
    print()
#####################################
print("Third row data:")
for i in range(n):
    for j in range(n):
        if i==2:
            print(mat[i][j],end=" ")
    print()
#####################################
print("First column data:")
for i in range(n):
    for j in range(n):
        if j==0:
            print(mat[i][j],end=" ")
        else:
            print("",end=" ")
    print()
#####################################
print("Second column data:")
for i in range(n):
    for j in range(n):
        if j==1:
            print(mat[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
#####################################
print("Third column data:")
for i in range(n):
    for j in range(n):
        if j==2:
            print(mat[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
#####################################
print("Right diagonal data:")
for i in range(n):
    for j in range(n):
        if i==j:
            print(mat[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
#####################################
print("Left diagonal data:")
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(mat[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
#####################################
print("Hollow Square: ")
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(mat[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
#####################################
print("Rigth triangle: ")
for i in range(n):
    for j in range(i+1):
        print(mat[i][j],end=" ")
    print()
#####################################
print("Rigth triangle: upside-down")
for i in range(n):
    for j in range(n-i):
        print(mat[i][j],end=" ")
    print()
#####################################
print("Rigth triangle: left-right")
for i in range(n):
    print("  "*(n-i-1),end="")
    for j in range(i+1):
        print(mat[i][j],end=" ")
    print()    
#####################################
print("Rigth triangle: left-right upside-down")
for i in range(n):
    print("  "*i,end="")
    for j in range(n-i):
        print(mat[i][j],end=" ")
    print()
