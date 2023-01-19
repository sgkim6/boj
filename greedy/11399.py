N = int(input())
P = list(map(int, input().split()))


def result(N, P):
    P.sort()

    result = 0
    for i in P:
        result += i*N
        N -= 1

    return result


print(result(N, P))

#백준 실버4 그리디 알고리즘