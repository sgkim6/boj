def dfs(x, visited, arr):

    def shoot(x):
        left = 1
        right = 1
        tmp[-(x+1)] = 0
        for i in range(-(x+1), -N-1, -1):  # 왼쪽탐색
            if tmp[i] != 0:
                left = tmp[i]
                break

        for i in range(-(x+1), 0, 1):  # 왼쪽탐색
            if tmp[i] != 0:
                right = tmp[i]
                break

        return left*right

    if visited == (1 << N) - 1:
        return arr[-(x+1)]

    if dp[x][visited] > 0:
        return dp[x][visited]

    for i in range(0, N):
        tmp = arr[:]
        if visited & (1 << i):
            continue
        score = shoot(i)
        dp[x][visited] = max(dp[x][visited], dfs(
            i, visited | (1 << i), tmp[:]) + score)

    return dp[x][visited]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 풍선 갯수
    arr = list(map(int, input().split()))
    answer = []
    for case in range(N):
        dp = [[0 for i in range(1 << (N+1))] for j in range(N)]
        #print((dfs(case, 1 << case, arr)))
        answer.append((dfs(case, 1 << case, arr)) + arr[-case-1])
    print(f"#{test_case} {max(answer)}")
