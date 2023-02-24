import sys
import heapq
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


V, E = map(int, input().split())
parent = [i for i in range(0, V+1)]
heap = []
answer = 0

for _ in range(E):
    start, end, cost = map(int, input().split())
    heapq.heappush(heap, (cost, start, end))

count = 0
while count < V-1:
    tmp = heapq.heappop(heap)

    if find(tmp[1]) != find(tmp[2]):  # 사이클이 안 만들어지면
        union(tmp[1], tmp[2])
        count += 1
        answer += tmp[0]
print(answer)
