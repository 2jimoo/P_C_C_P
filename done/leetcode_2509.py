'''
    https://leetcode.com/problems/cycle-length-queries-in-a-tree/
    https://leetcode.com/problems/cycle-length-queries-in-a-tree/solutions/2923489/java-c-python-lowest-common-ancestor/?orderBy=most_votes
    lca는 아니고 그 원리
    [방법1] 같아지기 전까지 큰 쪽을 하나씩 올린다.
    [방법2] a <= b 유지 -> 높이 맞추기 -> 공통 조상 찾기
'''
import math
from typing import List


class Solution:
    def get_dist(self, a, b) -> int:
        # a <= b 유지
        if a > b:
            tmp = a
            a = b
            b = tmp
        dist = 0
        # 높이 맞추기
        while int(math.log2(a)) != int(math.log2(b)):
            b //= 2
            dist += 1
        # 공통 조상 찾기
        while a != b:
            a //= 2
            b //= 2
            if a != 0:
                dist += 1
            if b != 0:
                dist += 1
        return dist + 1

    def get_dist2(self, n, queries):
        res = []
        # 같아지기 전까지 큰 쪽을 하나씩 올린다.
        for x, y in queries:
            res.append(1)
            while x != y:
                x, y = min(x, y), max(x, y) // 2
                res[-1] += 1
        return res

    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        for q in queries:
            answer.append(self.get_dist(q[0], q[1]))
        return answer


if __name__ == '__main__':
    solution = Solution()
    for result in solution.cycleLengthQueries(n=5,
                                              queries=[[17, 21], [23, 5], [15, 7], [3, 21], [31, 9], [5, 15], [11, 2],
                                                       [19, 7]]):
        print(result)
