from collections import deque

N, M = map(int, input().split())

graph = []

count = 0

year = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(N):
    graph.append(list(map(int, input().split())))

for r in range(N):
    for c in range(M):
        if graph[r][c] > 0:
            count += 1

while True:
    year += 1
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                for i in range(4):
                    nr = r + dr[i]
                    nc = r + dc[i]
                    if nr < 0 or nr > N or nc < 0 or nc > M:
                        continue
                    if graph[nr][nc] <= 0:
                        continue
                    if graph[nr][nc] > 1:
                        graph[nr][nc] -= 1
                    elif graph[nr][nc] == 1:
                        graph[nr][nc] = -1

    for r in range(N):
        for c in range(M):
            if graph[r][c] < 0:
                graph[r][c] = 0
                count -= 1

    q = deque()
    for r in range(N):
        for c in range(M):
            if graph[r][c] > 0:
                tmp = 1
                q.append((r, c))
                visited = [[False for i in range(M)] for j in range(N)]
                visited[r][c] = True
                while(q):
                    cr, cc = q.popleft()
                    for i in range(4):
                        nr = cr + dr[i]
                        nc = cc + dc[i]
                        if nr < 0 or nr > N or nc < 0 or nc > M:
                            continue
                        if visited[nr][nc]:
                            continue

                        q.append((nr, nc))
                        visited[nr][nc] = True
                        tmp += 1
                if tmp != count:
                    print(year)
                break
