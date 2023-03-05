'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
[방법1]
- https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/11423/short-but-recursive-java-code-with-comments/?orderBy=most_votes
- prev 뒤에 head(tail)의 뒤 노드를 넣는다
[방법2]
- 포인터 2개, k개 진행후 k개 거꾸로 저장
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return Optional[ListNode()]
