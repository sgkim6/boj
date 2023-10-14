N, east, west, south, north = map(int, input().split())

east = east*0.01
west = west*0.01
south = south*0.01
north = north*0.01

probablities = [east, south, west, north]

answer = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

visited = [[False for i in range(2*N+1)] for j in range(2*N+1)]


def dfs(row, col, step, prob):
    global answer
    if step == N:
        answer += prob
        return
    for i in range(4):
        n_row = row + dr[i]
        n_col = col + dc[i]
        n_prob = prob * probablities[i]
        if visited[n_row][n_col]:
            continue
        visited[n_row][n_col] = True
        dfs(n_row, n_col, step+1, n_prob)
        visited[n_row][n_col] = False


visited[0][0] = True
dfs(0, 0, 0, 1)

print(answer)
