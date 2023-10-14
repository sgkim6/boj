from collections import defaultdict, deque

N = int(input())
M = int(input())

graph = defaultdict(list)  # 경로 저장

memo = [[0 for i in range(N+1)] for j in range(N+1)]  # 기본 부품 갯수 저장

default_components = set()  # 기본 부품인지 체크

q = deque()

in_degree = [0 for i in range(N+1)]  # 진입차수

for i in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))  # 재료, 갯수
    in_degree[X] += 1

for i in range(N+1):
    if in_degree[i] == 0:
        q.append(i)
        default_components.add(i)

while q:
    i = q.popleft()
    for target, requests in graph[i]:
        if i in default_components:  # 기본 부품이면
            memo[target][i] += requests
        else:
            for j in range(1, N+1):
                memo[target][j] += requests * memo[i][j]

        in_degree[target] -= 1

        if in_degree[target] == 0:
            q.append(target)

for i in range(1, N):
    if memo[N][i] != 0:
        print(i, memo[N][i])
