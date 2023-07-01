from collections import deque, defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)
in_degree = [0 for i in range(N+1)]
q = deque()
order = deque()
visited = [False for i in range(N+1)]

for _ in range(M):
    tmp = input().split()
    for i in range(1, len(tmp)-1):
        graph[int(tmp[i])].append(int(tmp[i+1]))
        in_degree[int(tmp[i+1])] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        visited[i] = True
        q.append(i)

while q:
    cur = q.popleft()
    order.append(cur)
    for i in graph[cur]:
        if not visited[i]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                visited[i] = True
                q.append(i)

if len(order) == N:
    for i in order:
        print(i)
else:
    print(0)
