import heapq


def solution(ability, number):
    heapq.heapify(ability)
    while number > 0:
        a, b = heapq.heappop(ability), heapq.heappop(ability)
        heapq.heappush(ability, a + b)
        heapq.heappush(ability, a + b)
        number -= 1
    answer = sum(ability)
    return answer
