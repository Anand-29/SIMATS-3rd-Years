def upleftd_lowrightd(maze,source,dest):
    i=source[0];j=source[1]
    while i<dest[0] and j<dest[1]:
        print(i,j)
        i+=1
        j+=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
def lowrightd_upleftd(maze,source,dest):
    i=source[0];j=source[1]
    while i>dest[0] and j>dest[1]:
        print(i,j)
        i-=1
        j-=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
def lowleftd_uprightd(maze,source,dest):
    i=source[0];j=source[1]
    while i>dest[0] and j<dest[1]:
        print(i,j)
        i-=1
        j+=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
def uprightd_lowleftd(maze,source,dest):
    i=source[0];j=source[1]
    while i<dest[0] and j>dest[1]:
        print(i,j)
        i+=1
        j-=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
def up(maze,source,dest):
    i=source[0];j=source[1]
    while i>dest[0]:
        print(i,j)
        i-=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
def down(maze,source,dest):
    i=source[0];j=source[1]
    while i<dest[0]:
        print(i,j)
        i+=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
def left(maze,source,dest):
    i=source[0];j=source[1]
    while j>dest[1]:
        print(i,j)
        j-=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
def right(maze,source,dest):
    i=source[0];j=source[1]
    while j<dest[1]:
        print(i,j)
        j+=1
    if i==dest[0] and j==dest[1]:
        print(i,j)
        return True
    return False
n=int(input("Enter the size: "))
maze=[[x*0 for x in range(n)] for y in range(n)]
source=list(map(int,input("Enter source: ").split()))
dest=list(map(int,input("Enter dest: ").split()))
print("upleftd_lowrightd: ")
if upleftd_lowrightd(maze,source,dest):
    print("Reached")
else:
    print("Not possible")
print("lowrightd_upleftd: ")
if lowrightd_upleftd(maze,source,dest):
    print("Reached")
else:
    print("Not possible")
print("lowleftd_uprightd: ")
if lowleftd_uprightd(maze,source,dest):
    print("Reached")
else:
    print("Not possible")
print("uprightd_lowleftd: ")
if uprightd_lowleftd(maze,source,dest):
    print("Reached")
else:
    print("Not possible")
print("up: ")
if up(maze,source,dest):
    print("Reached")
else:
    print("Not possible")
print("down: ")
if down(maze,source,dest):
    print("Reached")
else:
    print("Not possible")
print("left: ")
if left(maze,source,dest):
    print("Reached")
else:
    print("Not possible")
print("right: ")
if right(maze,source,dest):
    print("Reached")
else:
    print("Not possible")






    
    
    
    
    
    
    
    
    
    
