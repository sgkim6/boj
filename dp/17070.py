N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

dp = [[[0,0,0] for i in range(N+1)] for j in range(N+1)]

dp[1][2][0] = 1 #좌 상 대각

for i in range(1,N+1):
    for j in range(3,N+1):
        
        if graph[i-1][j-1] == 0:
            dp[i][j][0] = dp[i][j-1][2] + dp[i][j-1][0] # 좌 상 대각
        if graph[i-1][j-1] == 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if graph[i-1][j-1] == 0 and graph[i-2][j-1] == 0 and graph[i-1][j-2] == 0 :
            dp[i][j][2] = dp[i-1][j-1][2] + dp[i-1][j-1][1] + dp[i-1][j-1][0]
        
print(sum(dp[N][N]))