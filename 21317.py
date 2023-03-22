N = int(input())

stones = [(0, 0)]

for i in range(N-1):
    small, big = map(int, input().split())
    stones.append((small, big))

K = int(input())

if (N == 1):
    print(0)
elif (N == 2):
    print(stones[1][0])
else:
    normal_dp = [0] * (N+1)
    total_dp = [0] * (N+1)
    normal_dp[1] = 0
    normal_dp[2] = stones[1][0]
    total_dp[1] = 0
    total_dp[2] = stones[1][0]
    total_dp[3] = min(stones[1][1], stones[1][0] + stones[2][0])

    for i in range(3, N+1):
        normal_dp[i] = min(normal_dp[i-2] + stones[i-2][1],
                           normal_dp[i-1] + stones[i-1][0])

    for i in range(4, N+1):
        total_dp[i] = min(total_dp[i-1] + stones[i-1][0], total_dp[i-2] +
                          stones[i-2][1], normal_dp[i-3] + K)

    print(total_dp[N])
