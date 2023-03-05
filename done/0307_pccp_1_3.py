def go(g, p, base):
    # 1세대
    if g == 1:
        return "Rr"
    # 2세대: 1세대의 p번째 자식
    elif g == 1:
        return base["Rr"][p]
    # 3세대 이후
    # 내 부모 par: g-1 세대 par_order 번째
    ch_order = p & 3
    par_order = p // 4 + (1 if ch_order != 0 else 0)
    par = go(g - 1, par_order, base)
    # 나는 par의 ch_order 번째 자식
    ch = base[par][ch_order]
    return ch


def solution(queries):
    base = {"RR": ["RR"] * 5, "Rr": ["rr", "RR", "Rr", "Rr", "rr"], "rr": ["rr"] * 5}
    answer = []
    for q in queries:
        g, p = q[0], q[1]
        ans = go(g, p, base)
        answer.append(ans)
    return answer


if __name__ == '__main__':
    answer = solution([[3, 8], [2, 2]])
    for ans in answer:
        print(ans)