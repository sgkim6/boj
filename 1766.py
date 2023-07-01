from collections import deque, defaultdict
import heapq

N, M = map(int, input().split())

graph = defaultdict(list)
in_degree = [0 for i in range(N+1)]
q = []
order = deque()
visited = [False for i in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        visited[i] = True
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    order.append(cur)
    for i in graph[cur]:
        if not visited[i]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                visited[i] = True
                heapq.heappush(q, i)


for i in order:
    print(i, end=" ")
