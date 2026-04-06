#rat in a maze
def safe(maze,r,c):
    if r<=4 and r>=0 and c<=4 and c>=0 and maze[r][c]==0:
        return True
    return False
def solution(maze,sol,r,c):
    if r==4 and c==4 and maze[r][c]==0:
        sol[r][c]=1
        return True
    if safe(maze,r,c)==True:
        sol[r][c]=1
        if solution(maze,sol,r,c+1)==True:
            return True
        if solution(maze,sol,r+1,c)==True:
            return True
        sol[r][c]=0
    return False
maze=[[0,0,0,0,0],
      [1,0,1,1,0],
      [1,0,0,1,1],
      [0,1,0,1,0],
      [0,1,0,0,0]]
sol=[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]
curr_row=0
curr_col=0
solution(maze,sol,curr_row,curr_col)
for i in range(5):
    for j in range(5):
        print(sol[i][j],end=" ")
    print()
