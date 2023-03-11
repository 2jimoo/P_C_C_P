# https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/
# rowShift - 행(리스트)의 인덱스만 관리
# rotate - list를 dequeue으로 써서 윗행 pop_back-> 아래행 push_back, 아래행 pop_front -> 윗행 push_front
def solution(rc, operations):
    answer = [[]]
    return answer