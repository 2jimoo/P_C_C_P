# https://school.programmers.co.kr/learn/courses/30/lessons/118668

# 출발 지점(alp, cpo) -> 목표지점(MAX_ALP, MAX_COP)
# problems에 문제 2개(alp++, cop++) 임의 추가, 상한값 clip

# 1. DP 시간초과(450*450*100)
#   바로 리턴? https://school.programmers.co.kr/questions/42502
# 2. 다익스트라 O(ElogV)
#   visited[코딩력][알고력] = true라면 재방문 할 필요가 없었습니다~~
#   PriorityQueue의 정렬조건에서 time을 기준으로 minHeap을 하게 되면
#   특정 코딩력, 알고력을 가질 수 있는 가장 작은 시간으로 처음 방문하게 됩니다
#   그리고 나서는 해당 시간보다 크거나 같기 때문에 한번 더 방문할 필요가 없게 됩니다!
import heapq


def solution(alp, cop, problems):
    INF = 10 ** 9
    max_alp, max_cop, answer = alp, cop, INF  # 0, 0, INF
    dp = [[INF] * 152 for _ in range(152)]
    for p in problems:
        max_alp = max(p[0], max_alp)
        max_cop = max(p[1], max_cop)
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i == max_alp and j == max_cop:
                return dp[i][j]
            for p in problems:
                if p[0] > i or p[1] > j:
                    continue
                next_alp = min(max_alp, i + p[2])
                next_cop = min(max_cop, j + p[3])
                dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + p[4])
    return answer


def solution2(alp, cop, problems):
    max_alp, max_cop = max(x[0] for x in problems), max(x[1] for x in problems)
    table = [[int(1e9) for _ in range(151)] for _ in range(151)]
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    h = [(0, alp, cop)]
    table[alp][cop] = 0
    while h:
        curr_cost, curr_alp, curr_cop = heapq.heappop(h)
        if curr_alp >= max_alp and curr_cop >= max_cop:
            return curr_cost
        if table[curr_alp][curr_cop] <= curr_cost:
            for r_alp, r_cop, a_alp, a_cop, n_cost in problems:
                n_alp, n_cop = min(150, curr_alp + a_alp), min(150, curr_cop + a_cop)
                if curr_alp >= r_alp and curr_cop >= r_cop and curr_cost + n_cost < table[n_alp][n_cop]:
                    table[n_alp][n_cop] = curr_cost + n_cost
                    heapq.heappush(h, (curr_cost + n_cost, n_alp, n_cop))
