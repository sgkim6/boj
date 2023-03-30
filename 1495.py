N, S, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[-1 for j in range(M+1)] for i in range(N+1)]
dp[0][S] = S

for row in range(N):
    for col in range(M+1):
        if(dp[row][col] != -1):
            if(col-arr[row] >= 0):
                dp[row+1][col-arr[row]] = dp[row][col] - arr[row]
            if(col+arr[row] <= M):
                dp[row+1][col+arr[row]] = dp[row][col] + arr[row]

print(max(dp[-1]))
