#n queens
def safe(sol,r,c):
    i=r;j=c
    while j>=0:
        if sol[i][j]!=0:
            return False
        j-=1
    i=r;j=c
    while i>=0 and j>=0:
        if sol[i][j]!=0:
            return False
        i-=1;j-=1
    i=r;j=c
    while i<=3 and j>=0:
        if sol[i][j]!=0:
            return False
        i+=1;j-=1
    return True
def solution(sol,c):
    if c==4:
        return True
    for i in range(4):
        if safe(sol,i,c):
            sol[i][c]=1
            if solution(sol,c+1)==True:
                return True
        sol[i][c]=0
    return False
sol=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
c=0
solution(sol,c)
for i in range(4):
    for j in range(4):
        print(sol[i][j],end=" ")
    print()
