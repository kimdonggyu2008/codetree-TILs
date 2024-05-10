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

import sys

INT_MIN = -sys.maxsize


def find_max_sum(matrix):
    n, m = len(matrix), len(matrix[0])
    msisdp = [[0 for _ in range(m)] for _ in range(n)]  # Maximum Sum in Single Subarray (DP table)
    max_size = 0
    max_so_far = INT_MIN

    for i in range(n):
        for j in range(m):
            msisdp[i][j] = matrix[i][j]

            if i > 0 and msisdp[i - 1][j] > 0:
                msisdp[i][j] += msisdp[i - 1][j]

    for i in range(n):
        for j in range(m):
            if msisdp[i][j] > max_so_far:
                max_so_far = msisdp[i][j]
                max_size = (i + 1) * (j + 1)

    return max_size


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    result = find_max_sum(matrix)
    print(result)
"""