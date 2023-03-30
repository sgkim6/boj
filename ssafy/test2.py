from collections import defaultdict
import sys
import heapq

N = int(input())
M = int(input())
graph = defaultdict(list)
INF = 999999999
distance = [INF for _ in range(N+1)]
min_heap = []

for _ in range(M):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))  # 거리, 도착지

start, end = map(int, input().split())

distance[start] = 0

heapq.heappush(min_heap, (0, start))

while min_heap:
    cur_dist, cur_node = heapq.heappop(min_heap)

    if distance[cur_node] < cur_dist:
        continue

    for next_node, next_dist in graph[cur_node]:
        if distance[next_node] > cur_dist + next_dist:
            distance[next_node] = cur_dist + next_dist
            heapq.heappush(min_heap, (distance[next_node], next_node))

print(distance[end])
