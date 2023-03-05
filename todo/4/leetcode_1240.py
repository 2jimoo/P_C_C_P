# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/solutions/414260/8ms-memorized-backtrack-solution-without-special-case/?orderBy=most_votes
# 댓글이 더 알기 쉬움
# [개념] 해싱, 휴리스틱, 백트래킹, map(dict)
#   0. dp<board_hash, count>
#   1. 각 높이를 h[n]로 저장
#   2. 현재의 보드는 h[]를 m+1을 base로 해싱한 것(14^14 Long 이내)
#      이 동안 최소 높이와 그 위치를 찾는다.(bottom-left에서 가장 큰 정사각형부터 채워볼 것)
#   3. 현재 방문 cnt보다 작은 값으로 방문한 적있거나, 글로벌 정답 이상이거나 최소 높이가 m이면 dp 갱신 후 리턴
#   6. pos에서 연속한 높이가 끝나는 end를 찾는다.
#      end -> pos 방향으로 높이 누적해서 다음 탐색해본다(copy필요)
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        return 0
