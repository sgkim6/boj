from collections import defaultdict
import heapq

N, D = map(int, input().split())

graph = defaultdict(list)
q = []  # dist, node
distance = [9999999] * 10001

for _ in range(N):
    start, end, dist = map(int, input().split())
    if dist >= start+end:
        continue

    graph[start].append((end, dist))

heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
    cur_dist, cur_node = heapq.heappop(q)
    if cur_node == D:
        print(cur_dist)
        break
    if cur_node > 10000:
        continue
    if cur_dist > distance[cur_node]:
        continue

    if cur_dist + 1 < distance[cur_node+1]:
        distance[cur_node+1] = cur_dist + 1
        heapq.heappush(q, (cur_dist + 1, cur_node+1))

    if cur_node in graph:  # 현재 위치에서 지름길이 있으면
        for load in graph[cur_node]:
            if cur_dist + load[1] < distance[load[0]]:
                distance[load[0]] = cur_dist + load[1]
                heapq.heappush(
                    q, (cur_dist + load[1], load[0]))
