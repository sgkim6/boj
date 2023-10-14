from collections import defaultdict, deque

N, M = map(int, input().split())

direction = [1, 2, 4, 8]  # 서 북 동 남
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

size_map = defaultdict(int)  # key : 방 번호, value : 방 넓이

graph = []
index_graph = [[0 for i in range(N)] for j in range(M)]
visited = [[False for i in range(N)] for j in range(M)]

idx = 1
answer = 0

for i in range(M):
    graph.append(list(map(int, input().split())))

for row in range(M):
    for col in range(N):
        if visited[row][col]:
            continue
        s = 1
        q = deque()
        visited[row][col] = True
        q.append((row, col))
        index_graph[row][col] = idx

        while q:
            c_row, c_col = q.popleft()
            for i in range(4):
                n_row = c_row + dr[i]
                n_col = c_col + dc[i]
                if n_row < 0 or n_row >= M or n_col < 0 or n_col >= N:
                    continue
                if visited[n_row][n_col]:
                    continue
                if graph[c_row][c_col] & direction[i] > 0:
                    continue
                q.append((n_row, n_col))
                visited[n_row][n_col] = True
                s += 1
                index_graph[n_row][n_col] = idx
        size_map[idx] = s
        idx += 1


for row in range(M):
    for col in range(N):
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            if n_row < 0 or n_row >= M or n_col < 0 or n_col >= N:
                continue
            if graph[c_row][c_col] & direction[i] == 0:
                continue
            if index_graph[row][col] == index_graph[n_row][n_col]:
                continue
            answer = max(
                answer, size_map[index_graph[row][col]] +
                size_map[index_graph[n_row][n_col]]
            )

print(size_map)
print(len(list(size_map.keys())))
print(max(list(size_map.values())))
print(answer)
