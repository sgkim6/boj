from collections import defaultdict, deque
import heapq

INF = 999999999

T = int(input())

for test_case in range(1, T+1):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    dist = [INF for j in range(n+1)]
    dist[c] = 0
    pq = []
    heapq.heappush(pq, (0, c))

    while pq:
        c_dist, c_node = heapq.heappop(pq)

        if dist[c_node] < c_dist:
            continue

        for n_dist, n_node in graph[c_node]:
            if dist[n_node] > c_dist + n_dist:
                dist[n_node] = c_dist + n_dist
                heapq.heappush(pq, (c_dist+n_dist, n_node))

    count = 0
    answer = 0
    for i in dist[1:]:
        if i != INF:
            count += 1
            answer = max(i, answer)

    # print(dist)
    print(count, answer)
