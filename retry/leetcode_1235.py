# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/409009/java-c-python-dp-solution/?orderBy=most_votes
# zip, tree map= bisect+append, floorKey/lowerKey/firstKey(이하, 미만, 최소)
# 정렬기준 dp: start, bottom-up: start하고 뒤에서 부터 채우거나 end 순
# 시간 순 [-1]:직전/현재 최대값
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        return 0
