# 1 0001 서
# 2 0010 북
# 4 0100 동
# 8 1000 남
from collections import deque, defaultdict


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
# 칸값을 2진수 리스트로 담고 4방향 중 0인 방향만 bfs돌리기
direction = [1, 2, 4, 8]
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def bfs(i, j, r):
    queue = deque()
    visited[i][j] = r
    queue.append((i, j))

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            # 벽이면 패쓰
            nx = x+dr[k]
            ny = y+dc[k]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] != 0:
                continue
            if graph[x][y] & direction[k] > 0:
                continue
            cnt += 1
            visited[nx][ny] = r
            queue.append((nx, ny))

    return cnt


visited = [[0 for _ in range(N)] for _ in range(M)]
room = defaultdict(int)
r = 0
for row in range(M):
    for col in range(N):
        if visited[row][col] != 0:
            continue
        r += 1

        room[r] = bfs(row, col, r)

result = 0

for row in range(M):
    for col in range(N):
        for k in range(4):
            # 벽일때 체크
            n_row = row+dr[k]
            n_col = col+dc[k]

            if n_row < 0 or n_row >= M or n_col < 0 or n_col >= N:
                continue
            # 같은방이면 패쓰
            if visited[row][col] == visited[row][col]:
                continue
            if graph[row][col] & direction[k] == 0:
                continue
            result = max(result, room[visited[row][col]
                                      ] + room[visited[n_row][n_col]])

# for i in range(m):
#     print(*visited[i])
# print(room)

print(len(list(room.keys())))
print(max(list(room.values())))
print(result)
