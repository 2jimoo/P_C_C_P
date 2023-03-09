def is_available(_y, _x, board):
    # padding 범위 제외
    return 0 < _y < len(board) and 0 < _x < len(board[0]) and board[_y][_x] != -1


def solution(w, h, hole):
    MAX = 10 ** 9
    board = [[0] * (w + 1) for _ in range(h + 1)]
    visit = [[[MAX] * 2 for _ in range(w + 1)] for _ in range(h + 1)]
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    jumps = [[2, 0], [0, 2], [-2, 0], [0, -2]]
    for hole_ in hole:
        board[hole_[1]][hole_[0]] = -1

    queue = [[1, 1, 0]]  # y, x, jump count
    visit[1][1][0] = 0
    while len(queue) > 0:
        y, x, cnt = queue[0][0], queue[0][1], queue[0][2]
        queue.pop(0)
        for d in dirs:
            ny, nx, ncnt = y + d[0], x + d[1], cnt
            if is_available(ny, nx, board) and visit[ny][nx][ncnt] == MAX:
                visit[ny][nx][ncnt] = visit[y][x][cnt] + 1
                queue.append([ny, nx, ncnt])
        if cnt == 0:
            for jp in jumps:
                jy, jx, jcnt = y + jp[0], x + jp[1], 1
                if is_available(jy, jx, board) and visit[jy][jx][jcnt] == MAX:
                    visit[jy][jx][jcnt] = visit[y][x][cnt] + 1
                    queue.append([jy, jx, jcnt])
    answer = min(visit[-1][-1][0], visit[-1][-1][1])
    return -1 if answer == MAX else answer
