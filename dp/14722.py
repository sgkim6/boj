N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

dp = [[0 for i in range(N)] for j in range(N)]

pre = 0
count = 0

for i in range(0, N):
    if graph[0][i] == pre:
        count += 1
        pre = (pre+1) % 3
    dp[0][i] = count

pre = 1
count = 1

for i in range(1, N):
    if graph[i][0] == pre:
        count += 1
        pre = (pre+1) % 3
    dp[i][0] = count

for row in range(1, N):
    for col in range(1, N):
        if (graph[row][col] - graph[row-1][col]) % 3 == 1:
            dp[row][col] = max(dp[row][col], dp[row-1][col]+1)
        if (graph[row][col] - graph[row][col-1]) % 3 == 1:
            dp[row][col] = max(dp[row][col], dp[row][col-1]+1)

for i in dp:
    print(i)
