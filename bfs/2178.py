from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]  # 우, 상, 왼, 하
L = []

N, M = map(int, input().split())

for i in range(N):
    s = input()
    s = list(s)
    s = list(map(int, s))
    L.append(s)


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if L[nx][ny] == 0:
                continue
            if L[nx][ny] == 1:
                L[nx][ny] = L[x][y]+1
                q.append((nx, ny))

    return L[N-1][M-1]


print(bfs(0, 0))
