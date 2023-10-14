from itertools import combinations
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = 0

graph = []
for i in range(5):
    graph.append(input())

b_graph = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

for numbers in combinations(range(25), 7):
    for number in numbers:
        b_graph[number//5][number % 5] = 1

    som = 0
    yeon = 0

    visited = [[False for i in range(5)] for j in range(5)]
    q = deque()
    q.append((numbers[0]//5, numbers[0] % 5))
    visited[numbers[0]//5][numbers[0] % 5] = True
    tmp = 1
    if graph[numbers[0]//5][numbers[0] % 5] == 'S':
        som += 1
    else:
        yeon += 1

    while q:
        c_row, c_col = q.popleft()
        for i in range(4):
            n_row = c_row + dr[i]
            n_col = c_col + dc[i]
            if n_row < 0 or n_row >= 5 or n_col < 0 or n_col >= 5:
                continue
            if visited[n_row][n_col]:
                continue
            if b_graph[n_row][n_col] == 0:
                continue
            visited[n_row][n_col] = True
            if graph[n_row][n_col] == 'S':
                som += 1
            else:
                yeon += 1
            tmp += 1
            q.append((n_row, n_col))
    if tmp == 7:
        if som >= 4:
            answer += 1

    for number in numbers:
        b_graph[number//5][number % 5] = 0

print(answer)
