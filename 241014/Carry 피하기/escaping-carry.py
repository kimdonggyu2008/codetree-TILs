from itertools import combinations

def carry(a,b):
    while a>0 or b>0:
        digit_a=a%10
        digit_b=b%10
        if digit_a+digit_b>=10:
            return False
        a//=10
        b//=10
    return True


def max_no_carry_numbers(numbers):
    n=len(numbers)
    max_count=0

    for r in range(1,n+1):
        for comb in combinations(numbers,r):
            valid_comb=True
            for i in range(len(comb)):
                for j in range(i+1,len(comb)):
                    if not carry(comb[i],comb[j]):
                        valid_comb=False
                        break
                if not valid_comb:
                    break

            if valid_comb:
                max_count=max(max_count,len(comb))
    return max_count


a=int(input())
n=[]
for i in range(a):
    n.append(int(input()))

result=max_no_carry_numbers(n)
print(result)