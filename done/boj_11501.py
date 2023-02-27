import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().split()))
    days.reverse()
    sumV = 0
    while days:
        key = max(days)
        where_key = days.index(key)
        sumV += key * (len(days)-where_key) - sum(days[where_key:])
        days = days[:where_key]
    print(sumV)


def go(prices, i, j) -> int:
    if i >= j:
        return 0
    max_val, max_idx = 0, -1
    for idx in range(i, j + 1):
        if max_val <= prices[idx]:
            max_val = prices[idx]
            max_idx = idx
    cost = sum(prices[i:max_idx])
    benefit = (max_idx - i) * max_val - cost
    benefit = benefit if benefit > 0 else 0
    return benefit+ go(prices, max_idx + 1, j)


if __name__ == '__main__':
    T = int(input())
    while T > 0:
        N = int(input())
        prices = list(map(int, input().split()))
        print(go(prices, 0, len(prices)-1))
        T -= 1
