import sys
import math
from itertools import combinations
input = sys.stdin.readline

T = int(input())


def com(score, case):
    tmp = 0
    for a, b in combinations(case, 2):
        tmp += score[a][b]
        tmp += score[b][a]
    return tmp


for test_case in range(1, T+1):
    N = int(input())
    score = []
    for _ in range(N):
        score.append(list(map(int, input().split())))

    answer = 999999999

    for case in combinations(range(N), N//2):
        another = list(set(range(N))-set(case))
        score_A = com(score, case)
        score_B = com(score, another)
        if answer > abs(score_A-score_B):
            answer = abs(score_A-score_B)
    print(f"#{test_case} {answer}")
