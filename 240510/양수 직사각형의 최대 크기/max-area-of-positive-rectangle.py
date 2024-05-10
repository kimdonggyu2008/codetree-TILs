"""
import sys
INT_MIN=-sys.maxsize

def howmuch(x1,y1,x2,y2):
    return sum([a[i][j] for i in range(x1,x2+1) for j in range(y1,y2+1)])


def find_max(n,m):
    max_sum=INT_MIN
    max_size=0
    for i in range(n):
        for j in range(m):
            for l in range(i,n):
                for k in range(j,m):
                    temp=howmuch(i,j,l,k)
                    if(temp>max_sum):
                        max_sum=temp
                        max_size=(l-i+1)*(k-j+1)
    if max_sum<0:
        max_size=-1
    return max_size



if __name__=="__main__":
    n,m=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    result=find_max(n,m)
    print(result)
"""

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
res = -1

def canCal(x, y, r, c):
    if 0 <= x and x + c < m and 0 <= y and y + r < n:
        return True
    else:
        return False

def cal(x, y, r, c):
    for i in range(c + 1):
        for j in range(r + 1):
            if matrix[y + j][x + i] <= 0:
                return False
    return True


def simul(x, y):
    global res
    for i in range(n):
        for j in range(m):
            if canCal(x, y, i, j):
                if cal(x, y, i, j):
                    res = max(res, (j+1) * (i+1))

for i in range(n):
    for j in range(m):
        simul(j, i)

print(res)