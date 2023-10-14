import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

dir = [1, 0, 3, 2]


def out(r, c):
    if r == -1:
        return 2*N + 2*M - c
    elif c == -1:
        return r+1
    elif r == N:
        return N + c + 1
    else:
        return 2*N + M - r


def search(start, direction):
    r, c = start
    while 0 <= r < N and 0 <= c < M:
        if board[r][c] == 1:
            direction = dir[direction]
        r += dr[direction]
        c += dc[direction]
    return str(out(r, c))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(N):
    direction = 1
    answer.append(search([i, 0], direction))
for i in range(M):
    direction = 0
    answer.append(search([N-1, i], direction))
for i in range(N-1, -1, -1):
    direction = 3
    answer.append(search([i, M-1], direction))
for i in range(M-1, -1, -1):
    direction = 2
    answer.append(search([0, i], direction))
print(' '.join(answer))
