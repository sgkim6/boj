from itertools import combinations

N = int(input())

graph = []

answer = int(1e9)

for i in range(N):
    graph.append(list(map(int, input().split())))

points = [(r, c) for r in range(1, N-1) for c in range(1, N-1)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for point_set in combinations(points, 3):
    if abs(point_set[0][0] - point_set[1][0]) + abs(point_set[0][1] - point_set[1][1]) <= 2:
        continue
    if abs(point_set[1][0] - point_set[2][0]) + abs(point_set[1][1] - point_set[2][1]) <= 2:
        continue
    if abs(point_set[2][0] - point_set[0][0]) + abs(point_set[2][1] - point_set[0][1]) <= 2:
        continue

    tmp = 0
    for r, c in point_set:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            tmp += graph[nr][nc]
        tmp += graph[r][c]

    answer = min(answer, tmp)

print(answer)
