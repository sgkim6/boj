import heapq

n, m, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]


for i in range(m):
    s, e, t = map(int, input().split())

    graph[s].append((t, e))


def dijkstra(start):
    q = []
    distance = [INF for _ in range(n+1)]

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        time, now = heapq.heappop(q)

        for i in graph[now]:
            next_t, next = i
            if distance[next] > time+next_t:
                distance[next] = time+next_t
                heapq.heappush(q, (distance[next], next))

    return distance  # 배열로 반환


result = 0
for i in range(1, n+1):
    go = dijkstra(i)[x]
    back = dijkstra(x)[i]

    result = max(result, go+back)

print(result)
