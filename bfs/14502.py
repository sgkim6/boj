from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
empty_list = []
virus_list = []
answers = []

max_space = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

for row in range(N):
    for col in range(M):
        if graph[row][col] == 0:
            empty_list.append((row, col))
        elif graph[row][col] == 2:
            virus_list.append((row, col))

empty_combinations = list(combinations(empty_list, 3))

for empty_set in empty_combinations:
    q = deque()

    cnt = 0
    tmp_graph = copy.deepcopy(graph)
    for location in empty_set:
        tmp_graph[location[0]][location[1]] = 1
    for location in virus_list:
        q.append((location[0], location[1]))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0 <= nr < N and 0 <= nc < M and tmp_graph[nr][nc] == 0:
                tmp_graph[nr][nc] = 2
                q.append((nr, nc))
    for row in tmp_graph:
        cnt += row.count(0)
    answers.append(cnt)

print(max(answers))
