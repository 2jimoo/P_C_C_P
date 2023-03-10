# https://school.programmers.co.kr/learn/courses/30/lessons/92345


def is_able_to_move(board, ny, nx):
    return 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == 1


def is_finished(board, y, x):
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for d in dirs:
        ny, nx = y + d[0], x + d[1]
        if is_able_to_move(board, ny, nx):
            return False
    return True


# 차례가 바뀌기 때문에 위치를 바꿔주는 아이디어도 있음
def go(board, y1, x1, y2, x2):
    # 같은 위치에 있는 경우 현재 플레이어가 이동 가능하면 승리한다.
    # 움직일 수 있는 곳이 없으면 진다.
    if is_finished(board, y1, x1):
        return False, 0
    if y1 == y2 and x1 == x2:
        return True, 1

    # 같은 위치가 아니라면
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    my_flag, max_play_cnt, min_play_cnt = False, 0, 10 ** 9
    for d in dirs:
        ny, nx = y1 + d[0], x1 + d[1]
        if not is_able_to_move(board, ny, nx):
            continue
        board[y1][x1] = 0
        opposite_flag, opposite_play_cnt = go(board, y2, x2, ny, nx)
        board[y1][x1] = 1
        # 상대가 진다 - 최대한 빨리 지게 만든다.
        if not opposite_flag:
            my_flag = True
            min_play_cnt = min(min_play_cnt, opposite_play_cnt)
        # 내가 진다 - 최대한 늦게 진다.
        else:
            max_play_cnt = max(max_play_cnt, opposite_play_cnt)
    return my_flag, (min_play_cnt if my_flag else max_play_cnt) + 1


def solution(board, aloc, bloc):
    return go(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]
