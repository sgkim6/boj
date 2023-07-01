from collections import deque

input_graph = []
graph = [[0 for i in range(8)] for j in range(8)]
visited = [[False for i in range(8)] for j in range(8)]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(8):
    input_graph.append(input())

for row in range(8):
    for col in range(8):
        if row == 0 or row == 7:
            graph[row][col] = 1 if input_graph[row][col] == '#' else 0
        else:
            if input_graph[row][col] == '#':
                graph[row][col] = 1
            else:
                if input_graph[row+1][col] == '#' and input_graph[row-1][col] == '#':
                    graph[row][col] = 1

col = 7
for row in range(8):
    if graph[row][col] == 1:
        for r in range(row, 8):
            graph[r][col] = 1
    col -= 1

q = deque()
q.append((7, 0))
visited[7][0] = True
answer = 0

while q:
    row, col = q.popleft()
    if row == 0:
        answer = 1
        break

    for i in range(8):
        n_row = row + dr[i]
        n_col = col + dc[i]

        if n_row < 0 or n_col < 0 or n_row >= 8 or n_col >= 8:
            continue

        if visited[n_row][n_col]:
            continue

        if graph[n_row][n_col] == 1:
            continue

        q.append((n_row, n_col))
        visited[n_row][n_col] = True

print(answer)
