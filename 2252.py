from collections import deque, defaultdict

N, M = map(int, input().split())

visited = [False for i in range(N+1)]

in_degree = [0 for i in range(N+1)]

graph = defaultdict(list)

q = deque()

answer = []

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    in_degree[end] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        visited[i] = True
        q.append(i)
        answer.append(i)

while q:
    node = q.popleft()
    for target in graph[node]:
        in_degree[target] -= 1
        if in_degree[target] == 0:
            visited[target] = True
            q.append(target)
            answer.append(target)

print(*answer)
