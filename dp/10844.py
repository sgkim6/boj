N = int(input())

dp = [[0 for i in range(N+1)] for j in range(10)]



for i in range(1,10):
    dp[i][1] = 1

for col in range(2,N+1):
    for row in range(0,10):
        if 1<=row<=8:
            dp[row][col] = (dp[row-1][col-1] + dp[row+1][col-1])
        elif row==0:
            dp[row][col] = (dp[row+1][col-1])
        elif row==9:
            dp[row][col] = (dp[row-1][col-1])

answer = 0
for i in range(10):
    answer += dp[i][N]
print(answer%1000000000)