from collections import deque, defaultdict

N, M, V = map(int, input().split())
graph = defaultdict(list)
visited = [0]*(N+1)


for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()


def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)


def bfs(start):
    q = deque()
    visited = [0]*(N+1)
    q.append(start)
    visited[start] = 1

    while q:
        tmp = q.popleft()
        print(tmp, end=' ')
        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


dfs(V)
print()
bfs(V)
