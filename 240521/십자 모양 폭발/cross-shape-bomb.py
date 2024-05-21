"""
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
    for i in range(n,0):
        for j in range(n,0):
            if(a[i][j]==0 and i!=0):
                print(i,j)
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
"""

# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


# 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
def cut_array(start_idx, end_idx):
    global end_of_array, numbers
    
    temp_arr = []
    
    # 구간 외의 부분만 temp 배열에 순서대로 저장합니다.
    for i in range(end_of_array):
        if i < start_idx or i > end_idx:
            temp_arr.append(numbers[i])

    # temp 배열을 다시 numbers 배열로 옮겨줍니다.
    end_of_array = len(temp_arr)
    for i in range(end_of_array):    
        numbers[i] = temp_arr[i]


# 두 번에 걸쳐 지우는 과정을 반복합니다.
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    # [s, e] 구간을 삭제합니다.
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])