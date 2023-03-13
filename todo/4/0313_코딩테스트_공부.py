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


def solution_dp(alp, cop, problems):
    return 0


def solution_dijkstra(alp, cop, problems):
    return 0