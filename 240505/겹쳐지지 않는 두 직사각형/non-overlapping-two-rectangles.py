import sys
INT_MIN=-sys.maxsize

def rect_sum(x1,y1,x2,y2):
    return sum([a[i][j] for i in range(x1,x2+1) for j in range(y1,y2+1)])

def clear_board():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0

def check_board():
    for i in range(n):
        for j in range(m):
            if(visited[i][j]>=2):
                return True
    return False

def draw(x1,y1,x2,y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            visited[i][j] += 1

def overlapped(x1,y1,x2,y2, i,j,k,l):
    clear_board()   # 모두 0으로 리셋 
    draw(x1,y1,x2,y2)
    draw(i,j,k,l)
    return check_board()

def find_max_sum_with_rect(x1,y1,x2,y2):
    max_sum = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    # overlapped은 겹치면 True 
                    if not overlapped(x1,y1,x2,y2, i,j,k,l):
                        max_sum = max(max_sum, rect_sum(x1,y1,x2,y2)+rect_sum(i,j,k,l))
    return max_sum 


if __name__=="__main__":
    n,m=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]

    visited=[[0]*m for _ in range(n)]


    max_sum=INT_MIN
    """
    for i in range(n):
        for j in range(m):
            for l in range(i,n):
                for k in range(j,m):
                    max_sum=max(max_sum,find_max_sum_with_rect(i,j,k,l))
    print(max_sum)
    """
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    max_sum = max(max_sum, find_max_sum_with_rect(i,j,k,l))
            
    print(max_sum)