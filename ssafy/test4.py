import math
from itertools import combinations

N = int(input())


def solution(N):
    if N == 0:
        print(0)
        return
    for digit in range(0, 10):  # 자릿수
        for i in range(1, 10):  # 첫번째 숫자
            N -= math.comb(i, digit)
            if N <= 0:
                tmp = [x for x in range(i-1, -1, -1)]
                number_set = list(combinations(tmp, digit))
                # print(digit, i)
                # print(number_set[-N])
                answer = str(i)
                for i in number_set[-N]:
                    answer += str(i)
                print(answer)
                return

    print(-1)


solution(N)
