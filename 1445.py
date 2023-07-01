import heapq

N, M = map(int, input().split())

graph = []

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
q = []

visited = [[False for i in range(M)] for j in range(N)]

for i in range(N):
    graph.append(list(input()))

for row in range(N):
    for col in range(M):
        if graph[row][col] == 'g':
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue

                if graph[nr][nc] != '.':
                    continue

                graph[nr][nc] = 'n'

        elif graph[row][col] == 'S':
            heapq.heappush(q, (0, 0, row, col))
            visited[row][col] = True

while q:
    x, y, row, col = heapq.heappop(q)
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        if visited[nr][nc]:
            continue

        if graph[nr][nc] == '.':
            heapq.heappush(q, (x, y, nr, nc))
            visited[nr][nc] = True
            continue

        if graph[nr][nc] == 'g':
            heapq.heappush(q, (x+1, y, nr, nc))
            visited[nr][nc] = True
            continue

        if graph[nr][nc] == 'n':
            heapq.heappush(q, (x, y+1, nr, nc))
            visited[nr][nc] = True
            continue

        if graph[nr][nc] == 'F':
            print(x, y)
            visited[nr][nc] = True
            continue
