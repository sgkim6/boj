N = int(input())
M = int(input())
vips = []
for i in range(M):
    vips.append(int(input()))

streak = 0
dp = [0] * (N+1)

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
if M >= 1:
    tmp = 0
    for i in range(M):
        answer *= dp[vips[i]-1-tmp]
        tmp = vips[i]
    answer *= dp[N-tmp]
else:
    answer = dp[N]
print(answer)
