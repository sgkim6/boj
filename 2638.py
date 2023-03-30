from collections import deque

N, M = map(int, input().split())

graph = []

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

time = 1

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs():
    visited = [[0 for j in range(M)] for i in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        row, col = q.popleft()

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[next_row][next_col] == 1:
                continue
            if graph[next_row][next_col] >= 1:
                graph[next_row][next_col] += 1
                continue
            q.append((next_row, next_col))
            visited[next_row][next_col] = 1

    for row in range(N):
        for col in range(M):
            if graph[row][col] >= 3:
                graph[row][col] = 0
            elif graph[row][col] == 2:
                graph[row][col] = 1


def checkClear():
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1:
                return False
    return True


while True:
    bfs()
    if checkClear():
        print(time)
        break
    else:
        time += 1
