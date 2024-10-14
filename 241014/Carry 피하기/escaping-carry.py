from itertools import combinations

def carry(a, b):
    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        if digit_a + digit_b >= 10:
            return False
        a //= 10
        b //= 10
    return True

def max_no_carry_numbers(numbers):
    n = len(numbers)
    max_count = 0
    dp = [0] * (1 << n)

    for mask in range(1, 1 << n):
        valid = True
        current_sum = 0
        for i in range(n):
            if mask & (1 << i):
                if not carry(current_sum, numbers[i]):
                    valid = False
                    break
                current_sum += numbers[i]
        if valid:
            dp[mask] = bin(mask).count('1')
            max_count = max(max_count, dp[mask])

    return max_count

a = int(input())
n = [int(input()) for _ in range(a)]

result = max_no_carry_numbers(n)
print(result)