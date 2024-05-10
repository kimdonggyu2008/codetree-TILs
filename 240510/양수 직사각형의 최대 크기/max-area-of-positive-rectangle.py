def howmuch(x1,y1,x2,y2):
    return sum([a[i][j] for i in range(x1,x2+1) for j in range(y1,y2+1)])


def find_max(n,m):
    max_sum=-9999999
    max_size=0
    for i in range(n):
        for j in range(m):
            for l in range(i,n):
                for k in range(j,m):
                    temp=howmuch(i,j,l,k)
                    if(temp>max_sum):
                        max_sum=temp
                        max_size=(l-i+1)*(k-j+1)

    return max_size



if __name__=="__main__":
    n,m=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    result=find_max(n,m)
    print(result)