def solution(menu, orders, k):
    psum = [0] * (len(orders)*k + max(menu)+1)
    doneTime = 0
    for idx, order in enumerate(orders):
        enter = idx * k
        doneTime = max(doneTime, enter) + menu[order]
        psum[enter] += 1
        psum[doneTime] -= 1
    cur, answer = 0, 0
    for p in psum:
        cur += p
        answer = max(answer, cur)
    return answer


if __name__ == '__main__':
    answer = solution([5], 	[0, 0, 0, 0, 0], 5)
    print(answer)