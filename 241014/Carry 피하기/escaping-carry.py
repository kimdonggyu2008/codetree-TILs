from itertools import combinations
from functools import lru_cache

def carry(a, b):
    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        if digit_a + digit_b >= 10:
            return False
        a //= 10
        b //= 10
    return True

@lru_cache(None)
def is_valid_combination(numbers):
    temp = 0
    for number in numbers:
        if not carry(temp, number):
            return False
        temp += number
    return True

def max_no_carry_numbers(numbers):
    n = len(numbers)
    max_count = 0

    for r in range(1, n + 1):
        for comb in combinations(numbers, r):
            if is_valid_combination(comb):
                max_count = max(max_count, len(comb))

    return max_count

a = int(input())
n = [int(input()) for _ in range(a)]

result = max_no_carry_numbers(tuple(n))
print(result)