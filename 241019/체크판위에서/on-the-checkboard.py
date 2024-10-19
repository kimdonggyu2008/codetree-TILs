r,c=map(int,input().split())

square=[list(input()) for _ in range(r)]
visited=[[False for _ in range(c)] for _ in range(c)]


def is_valid(x,y,color):
    return (square[x][y]!=color and 0<=x<r and 0<=y<c and not visited[x][y])


def backtrack(x,y):
    if x==r-1 and y==c-1:
        return 1
    visited[x][y]=True
    current_color=square[x][y]
    total_paths=0
    directions=[]

    for i in range(x,r-1):
        for j in range(y,c-1):
            #print(i,j)
            directions.append((r-i-1,c-j-1))

    #print(directions)

    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if is_valid(nx,ny,current_color):
            total_paths+=backtrack(nx,ny)
    visited[x][y]=False
    return total_paths

result=backtrack(0,0)
print(result)