import sys
input = sys.stdin.readline

N = int(input())

dp = []
dp.append(tuple(map(int, input().split())))
for i in range(N-1):
    tmp = tuple(map(int, input().split()))
    dp.append((min(dp[i][1], dp[i][2])+tmp[0], min(dp[i][0],
              dp[i][2])+tmp[1], min(dp[i][0], dp[i][1])+tmp[2]))

print(min(dp[-1]))
