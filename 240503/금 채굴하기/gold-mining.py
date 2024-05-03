n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
best=0

def biggest(x,y,k):#갯수 세기
    total=0
    for i in range(n):
        for j in range(n):
            if abs(x-i)+abs(y-j)<=k:#마름모 중간 기준 위치 다 보기
                total+=a[i][j]

    return total

def digprice(k):
    return k*k+(k+1)*(k+1)


for i in range(n):
    for j in range(n):
        for k in range(n):
            now=biggest(i,j,k)
            if((now*m)>=digprice(k) and best<=now):
                best=now
            if(best==(n*n)-1 and n!=1):
                best+=1

print(best)