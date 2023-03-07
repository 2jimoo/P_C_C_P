import heapq


# https://velog.io/@soorim_yoon/PCCP-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC-104-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C
def solution(program):
    answer = [0] * 11  # 프로그램 우선순위는 1~10번까지 존재하므로 (answer[0]은 최종 실행 시간)
    program.sort(key=lambda x: x[1])
    heap = []  # heapq의 경우 리스트를 사용해야 함
    cur = 0  # 현재 시각

    def put_program():  # program 배열 안의 프로그램을 pQ에 넣어주는 작업
        while len(program) > 0 and program[0][1] <= cur:
            heapq.heappush(heap, program.pop(0))

    while len(program) > 0 or not len(heap) == 0:
        if len(heap) == 0:  # pQ가 비어있다면
            cur = program[0][1]  # program 배열의 맨 앞의 값의 시각을 현재 시각으로 설정
            put_program()
        execute = heapq.heappop(heap)  # 가장 앞의 값을 제거
        answer[execute[0]] += (cur - execute[1])  # answer 배열의 해당 우선순위 인덱스에 대기 시간 값을 추가함
        cur += execute[2]  # 현재 시각을 갱신
        put_program()
    answer[0] += cur  # answer[0]은 모든 프로그램이 종료되는 시각
    return answer


def solution_tle(program):
    # 프로그램 시간 순 정렬 - 우큐 점수, 시간 순 정렬
    program.sort(key=lambda x: x[1])
    cnt, idx, done_time, cur_time = 0, 0, 0, 0
    heap, answer = [], [0] * 11
    while cnt < len(program):
        # 시간이 흐르며 현재 시간 이전 호출된 것들에 대해 우큐로 정렬
        while idx < len(program) and program[idx][1] <= cur_time:
            heapq.heappush(heap, ((program[idx][0], program[idx][1]), program[idx]))
            idx += 1
        # 하나만 뽑아 실행 하려는 데, 현재 시간이 마지막 실행 완료 시간 이상이 되어야 실행 가능
        if len(heap) > 0 and done_time <= cur_time:
            p = heapq.heappop(heap)[1]
            score, scheduled_time, duration = p[0], p[1], p[2]
            answer[score] += cur_time - scheduled_time
            done_time = cur_time + duration
            cnt += 1
        cur_time += 1
    answer[0] = done_time
    return answer


if __name__ == '__main__':
    print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
