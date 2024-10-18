n,d,k,c= map(int,input().split())

numbers = [int(input()) for _ in range(n)]

def count(numbers,k,n,c):
    most_diff=0
    temp_numbers=numbers+numbers[:k-1]
    for i in range(n):
        c_diff=0
        diff=set(temp_numbers[i:i+k])
        if c not in diff:
            c_diff=len(diff)+1
        else:
            c_diff=len(diff)

        most_diff=max(most_diff,c_diff)
    return most_diff

print(count(numbers,k,n,c))