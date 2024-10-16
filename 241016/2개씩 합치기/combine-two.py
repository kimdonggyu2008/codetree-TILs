n=int(input())
numbers = list(map(int, input().split()))  # 두 번째 입력은 숫자들을 공백으로 구분하여 입력

import heapq

def min_sum_of_merges(n, numbers):
    # 최소 힙으로 변환
    heapq.heapify(numbers)
    total_cost = 0

    # 힙에서 두 개씩 꺼내 합치고 다시 넣는 과정 반복
    while len(numbers) > 1:
        # 가장 작은 두 개의 원소를 꺼냄
        first = heapq.heappop(numbers)
        second = heapq.heappop(numbers)
        
        # 두 수를 합친 비용을 계산하고 총 비용에 추가
        cost = first + second
        total_cost += cost
        
        # 합친 결과를 다시 힙에 넣음
        heapq.heappush(numbers, cost)

    return total_cost


# 결과 출력
print(min_sum_of_merges(n, numbers))