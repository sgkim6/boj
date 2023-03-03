from collections import deque, Counter


def solution(N, stages):
    counter = Counter(stages)
    # stages.sort(reverse=True)
    answer = [0]*(N+1)
    failed = [0]*(N+1)
    tried = [0]*(N+1)
    for i in range(1, N+1):
        failed[i] = counter[i]
        tmp = 0
        for key, value in counter.items():
            if key >= i:
                tmp += value
        tried[i] = tmp

    for i in range(1, len(answer)):
        if tried[i] != 0:
            answer[i] = (failed[i]/tried[i], i)
        else:
            answer[i] = (0, i)

    answer = answer[1:]
    answer.sort(key=lambda x: (-x[0], x[1]))
    result = [0]*N
    for i in range(len(answer)):
        result[i] = answer[i][1]
    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
