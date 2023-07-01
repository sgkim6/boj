import heapq

q = []

heapq.heappush(q, (0, 0, 1))
heapq.heappush(q, (0, 0, 3))
heapq.heappush(q, (0, 0, 2))
heapq.heappush(q, (0, 0, 4))

while q:
    x, y, z = heapq.heappop(q)
    print(z)
