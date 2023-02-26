'''
https://leetcode.com/problems/rectangle-area-ii/
[주의점] 땅에 블록이 붙어 있는게 아니다. [[0,0,1,1],[2,2,3,3]]
비슷한 문제: https://leetcode.com/problems/meeting-rooms-iii/

[방법1] X방향 진행
    # 105 ms 14.3 MB
https://leetcode.com/problems/rectangle-area-ii/solutions/137941/java-treemap-solution-inspired-by-skyline-and-meeting-room/?orderBy=most_votes
- preY 탐색 필요함, y에 대한 treemap, x에 대한 정렬
- from collections import OrderedDict, from sortedcontainers import SortedDict(입력 순서, 키 순서)
[방법2] Y방향 진행
    # 65 ms 13.9 MB
https://leetcode.com/problems/rectangle-area-ii/solutions/137914/java-c-python-discretization-and-o-nlogn/?orderBy=most_votes
- {y, x1, x2, sig}, y순서 정렬
- (y-pre_y)*cur_sum
- sig를 [x1,x2]에 대해 누적
- cur_xum= 전체 구간합(세그먼트 트리 이용가능)
'''
from typing import List

from sortedcontainers import SortedDict


class Solution:
    def rectangleArea(self, rectangles):
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)

    def __init__(self):
        self.map = SortedDict()
        self.mod = 1000000000 + 7

    def find_preY(self):
        result, pre, count = 0, -1, 0
        for y, cnt in self.map.items():
            if pre >= 0 and count > 0:
                result += (y - pre)
            count += cnt
            pre = y
        return result
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        points = []
        for r in rectangles:
            points.append((r[0], r[1], 1))
            points.append((r[0], r[3], -1))
            points.append((r[2], r[1], -1))
            points.append((r[2], r[3], 1))
            self.map[r[3]] = 0
            self.map[r[1]] = 0
        points.sort(key=lambda p: p[0])
        preX, preY, result = -1, -1, 0
        for i, p in enumerate(points):
            x, y, sig = p[0], p[1], p[2]
            self.map[y] += sig
            if i == len(points) - 1 or points[i][0] < points[i + 1][0]:
                if preX > -1:
                    result = (result + (preY * (points[i][0] - preX)) % self.mod) % self.mod
                preY = self.find_preY()
                preX = p[0]
        return result


if __name__ == '__main__':
    solution = Solution()
    answer = solution.rectangleArea([[0, 0, 1, 1], [2, 2, 3, 3]])
    print(answer)
