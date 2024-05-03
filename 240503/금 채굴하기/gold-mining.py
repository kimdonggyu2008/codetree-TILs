n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

best=0

def biggest(k,x,y):
    total=0
    for i in range(n):
        for j in range(n):
            if abs(x-i)+abs(y-j)<=k:
                total+=a[i][j]
    return total

def digprice(k):
    return k*k+(k+1)*(k+1)


for i in range(n):
    for j in range(n):
        for k in range(n):
            if(biggest(k,i,j)*m>digprice(k)and best<biggest(k,i,j)):
                best=biggest(k,i,j)

print(best)