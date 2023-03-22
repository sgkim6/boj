import heapq

N, K = map(int, input().split())
moves = [lambda x:x*2, lambda x:x+1, lambda x:x-1]

q = []

distance = [999999999] * 100001
distance[N] = 0
heapq.heappush(q, (0, N))

while q:
    cur_dist, cur_node = heapq.heappop(q)
    if cur_dist > distance[cur_node]:
        continue

    for i in range(3):
        next_node = moves[i](cur_node)
        if next_node < 0 or next_node > 100000:
            continue

        if i == 0:
            if distance[next_node] > cur_dist + 0:  # teleport
                distance[next_node] = cur_dist
                heapq.heappush(q, (distance[next_node], next_node))
        else:
            if distance[next_node] > cur_dist + 1:  # normal move
                distance[next_node] = cur_dist + 1
                heapq.heappush(q, (distance[next_node], next_node))

print(distance[K])





