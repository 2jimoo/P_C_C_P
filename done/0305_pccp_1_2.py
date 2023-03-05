global dp
global students
global subjects


def go(student_mask, j, ability):
    global subjects, students, dp
    if j == subjects:
        return 0
    if dp[student_mask][j] != -1:
        return dp[student_mask][j]
    dp[student_mask][j] = 0
    for i in range(students):
        if (student_mask & (1 << i)) == 0:
            dp[student_mask][j] = max(dp[student_mask][j], go(student_mask | (1 << i), j + 1, ability) + ability[i][j])
    return dp[student_mask][j]


def solution(ability):
    global subjects, students, dp
    students = len(ability)
    subjects = len(ability[0])
    dp = [[-1] * subjects for _ in range((1 << students))]
    answer = go(0, 0, ability)
    return answer


if __name__ == '__main__':
    print(solution([[20, 30], [30, 20], [20, 30]]))
