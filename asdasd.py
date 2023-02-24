from collections import deque, Counter


def solution(N, stages):
    counter = Counter(stages)
    stages.sort(reverse=True)
    answer = [0]*(N+1)
    amount = counter[N+1]
    for i in range(N, 0, -1):
        amount += counter[i]
        answer[i] = counter[i] / amount

    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
