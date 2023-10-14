from collections import deque

N, M = map(int, input().split())

graph = [[0 for i in range(N+2)]]

for i in range(M):
    row_input = list(map(int, input().split()))
    graph.append([0] + row_input + [0])

graph.append([0 for i in range(N+2)])

dir_odd = [(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)]
dir_even = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]

visited = [[False for i in range(N+2)] for j in range(M+2)]

q = deque()

q.append((0, 0))

visited[0][0] = True

answer = 0

while q:
    row, col = q.popleft()
    if (row+1) % 2 == 0:
        for i in range(6):
            n_row = row + dir_even[i][0]
            n_col = col + dir_even[i][1]
            if n_row < 0 or n_row >= M+2 or n_col < 0 or n_col >= N+2:
                continue
            if visited[n_row][n_col]:
                continue
            if graph[n_row][n_col] == 1:
                answer += 1
                continue
            visited[n_row][n_col] = True
            q.append((n_row, n_col))
    else:
        for i in range(6):
            n_row = row + dir_odd[i][0]
            n_col = col + dir_odd[i][1]
            if n_row < 0 or n_row >= M+2 or n_col < 0 or n_col >= N+2:
                continue
            if visited[n_row][n_col]:
                continue
            if graph[n_row][n_col] == 1:
                answer += 1
                continue
            visited[n_row][n_col] = True
            q.append((n_row, n_col))

print(answer)
