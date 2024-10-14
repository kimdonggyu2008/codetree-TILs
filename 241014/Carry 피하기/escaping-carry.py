# from itertools import combinations

# def carry(a,b):
#     while a>0 or b>0:
#         digit_a=a%10
#         digit_b=b%10
#         if digit_a + digit_b>=10:
#             return False
#         a//=10
#         b//=10
#     return True


# def max_no_carry_numbers(numbers):
#     n=len(numbers)
#     max_count=0

#     for r in range(1,n+1):
#         for comb in combinations(numbers,r):
#             valid_comb=True
#             for i in range(len(comb)):
#                 for j in range(i,len(comb)):
#                     temp=sum(comb[:i])
#                     if not carry(temp,comb[j]):
#                         valid_comb=False
#                         break
#                 if not valid_comb:
#                     break

#             if valid_comb:
#                 max_count=max(max_count,len(comb))
#     return max_count


# a=int(input())
# n=[]
# for i in range(a):
#     n.append(int(input()))

# result=max_no_carry_numbers(n)
# print(result)
from itertools import combinations

# Carry가 발생하는지 확인하는 함수
def carry(a, b):
    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        if digit_a + digit_b >= 10:
            return False
        a //= 10
        b //= 10
    return True

# Carry가 발생하지 않는 최대 조합의 크기 계산
def max_no_carry_numbers(numbers):
    n = len(numbers)
    max_count = 0

    # 숫자들 간 carry가 발생하지 않는지 미리 계산해서 캐싱
    carry_matrix = [[True] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            carry_matrix[i][j] = carry(numbers[i], numbers[j])

    # 숫자들을 1개부터 n개까지 조합하여 carry가 발생하지 않는 최대 크기 찾기
    for r in range(1, n + 1):
        for comb in combinations(range(n), r):
            valid_comb = True
            for i in range(len(comb)):
                for j in range(i + 1, len(comb)):
                    if not carry_matrix[comb[i]][comb[j]]:
                        valid_comb = False
                        break
                if not valid_comb:
                    break
            if valid_comb:
                max_count = max(max_count, len(comb))
                
    return max_count

# 입력 받기
a = int(input())
n = [int(input()) for _ in range(a)]

# 결과 출력
result = max_no_carry_numbers(n)
print(result)