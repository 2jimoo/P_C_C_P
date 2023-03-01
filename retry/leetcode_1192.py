'''
https://leetcode.com/problems/critical-connections-in-a-network/
[문제] 삭제하면 어떤 노드 쌍의 직간접적 경로가 사라지는 엣지 반환
방법2) SCC 타잔 알고리즘
 - SCC의 정의= 그래프에서 어떤 노드쌍이든 직간접적으로 연결되어있는 부분
 - 코사라주 알고리즘(https://jooona.tistory.com/159)보다는 타잔 알고리즘이 구현이 어렵지만 활용도가 더 높다(https://yjg-lab.tistory.com/188)
https://leetcode.com/problems/critical-connections-in-a-network/solutions/382632/java-implementation-of-tarjan-algorithm-with-explanation/?orderBy=most_votes
방법1) 이 노드 방문하는 최소한의 타이머 갱신
 - 내 자식이 나보다 타임스탬프가 크다면 반드시 나를 통해서 지나가야하므로  (나, 그 자식)은 중요 연결이다.
https://leetcode.com/problems/critical-connections-in-a-network/solutions/401340/clean-java-solution-with-explanation-great-question/?orderBy=most_votes
'''
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        return []


if __name__ == '__main__':
    solution = Solution()
    n = 10
    connections = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 3], [6, 1], [7, 2], [8, 1], [9, 6], [9, 3], [3, 2], [4, 2],
                   [7, 4], [6, 2], [8, 3], [4, 0], [8, 6], [6, 5], [6, 3], [7, 5], [8, 0], [8, 5], [5, 4], [2, 1],
                   [9, 5], [9, 7], [9, 4], [4, 3]]
    answer = solution.criticalConnections(n, connections)
    for a, b in answer:
        print("%d %d" % (a, b))
