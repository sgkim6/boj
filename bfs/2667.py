from collections import deque

N = int(input())

graph = []
num = 2

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for _ in range(N):
    graph.append(list(input()))

visited = [[0]*N for i in range(N)]

for row in range(N):
    for col in range(N):
        graph[row][col] = int(graph[row][col])

for row in range(N):
    for col in range(N):

        if visited[row][col] == 0 and graph[row][col] == 1:
            visited[row][col] = 1
            graph[row][col] = num
            q = deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                for i in range(4):
                    nr = r+dr[i]
                    nc = c+dc[i]
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and graph[nr][nc] == 1:
                        visited[nr][nc] = 1
                        graph[nr][nc] = num
                        q.append((nr, nc))
            num += 1


max_value = max(map(max, graph))
print(max_value-1)
answer = []
for i in range(2, max_value+1):
    count = 0
    for row in range(N):
        count += graph[row].count(i)
    answer.append(count)
answer.sort()
for i in answer:
    print(i)
