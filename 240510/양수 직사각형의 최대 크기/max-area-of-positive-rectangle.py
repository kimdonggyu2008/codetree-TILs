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
                        #print("현재 위치", i,j,l,k)
                        #print(temp)
                        #print("가로세로",(l-i+1)*(k-j+1))
                        max_size=(l-i+1)*(k-j+1)

    return max_size



if __name__=="__main__":
    n,m=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    result=find_max(n,m)
    print(result)