from collections import defaultdict
import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

V, E = map(int, input().split())  # V : 정점의 갯수, E : 간선의 갯수

K = int(input())  # K : 시작점

# 초기화
graph = [[] for _ in range(V + 1)]
value = [INF]*(V+1)
q = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

heapq.heappush(q, (K, 0))
value[K] = 0
while q:
    v, w = heapq.heappop(q)
    if value[v] < w:
        continue

    for next_node, weight in graph[v]:
        next_weight = weight + w
        if next_weight < value[next_node]:  # 만약 이미 알고있는 최단거리보다 더 짧을 경우
            value[next_node] = next_weight
            heapq.heappush(q, (next_node, next_weight))

for i in range(1, V+1):
    if value[i] == INF:
        print('INF')
    else:
        print(value[i])
