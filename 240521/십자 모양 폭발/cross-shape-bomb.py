def boom(a,x,y,n):
    length=a[x-1][y-1]-1
    #print(x,y,length)
    top=max(x-length-1,0)
    bottom=min(x+length,n)
    left=max(y-length-1,0)
    right=min(y+length,n)
    #print("범위",top,bottom,left,right)
    for i in range(top,bottom):
        a[i][y-1]=0
    #a[x][bottom:top-1]=0
    for j in range(left,right):
        a[x-1][j]=0
    #a[left:right][y]=0
    return a

def drop(a,n):
    for i in range(n):
        for j in range(n):
            if(a[i][j]==0 and i!=0):
                #print(i,j)
                a[i][j]=a[i-1][j]
                a[i-1][j]=0
    return a

n=int(input())
a=[]
for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)
x,y=map(int,input().split())
a=boom(a,x,y,n)
a=drop(a,n)


for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print('')