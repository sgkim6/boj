from collections import deque

N = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
answer = int(1e9)

graph = []
visited = [[False for i in range(N)] for j in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))

num = 1
for row in range(N):
    for col in range(N):
        if visited[row][col]:
            continue
        if graph[row][col] == 0:
            continue
        q = deque()
        q.append((row, col, num))
        visited[row][col] = True
        graph[row][col] = num
        while q:
            c_row, c_col, c_num = q.popleft()
            for i in range(4):
                n_row = c_row + dr[i]
                n_col = c_col + dc[i]
                if n_row < 0 or n_col < 0 or n_row >= N or n_col >= N:
                    continue
                if visited[n_row][n_col]:
                    continue
                if graph[n_row][n_col] == 0:
                    continue

                graph[n_row][n_col] = num
                visited[n_row][n_col] = True
                q.append((n_row, n_col, c_num))
        num += 1


for row in range(N):
    for col in range(N):
        if graph[row][col] == 0:
            continue

        q = deque()
        visited = [[False for i in range(N)] for j in range(N)]
        num = graph[row][col]
        q.append((row, col, 0))

        while q:
            c_row, c_col, dist = q.popleft()
            for i in range(4):
                n_row = c_row + dr[i]
                n_col = c_col + dc[i]
                if n_row < 0 or n_col < 0 or n_row >= N or n_col >= N:
                    continue
                if visited[n_row][n_col]:
                    continue
                if graph[n_row][n_col] == num:  # 원래 섬으로 돌아온경우
                    continue
                if graph[n_row][n_col] != num and graph[n_row][n_col] != 0:
                    answer = min(answer, dist)

                visited[n_row][n_col] = True
                q.append((n_row, n_col, dist+1))

print(answer)
