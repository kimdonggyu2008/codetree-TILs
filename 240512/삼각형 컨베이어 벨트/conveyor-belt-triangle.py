n,t=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(3)]
for _ in range(t):
    last1=a[0][-1]
    last2=a[1][-1]
    last3=a[2][-1]
    for i in range(3):
        for j in range(n-1,0,-1):
            a[i][j]=a[i][j-1]
    a[0][0]=last3
    a[1][0]=last1
    a[2][0]=last2
for row in a:
    for column in row:
        print(column,end=' ')
    print()