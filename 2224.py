from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

INF = 999999999
N = int(input())
graph = defaultdict(list)

for _ in range(N):
    tmp = input().split()
    start = tmp[0]
    end = tmp[2]
    graph[start].append(end)


def chrToNumber(x):
    return ord(x)-65 if ord(x) <= 90 else ord(x)-71


def dijkstra(x):
    distance = [INF] * 52
    q = []

    q.append(x)
    distance[chrToNumber(x)] = 0

    while q:
        tmp = heapq.heappop(q)

        for node in graph[tmp]:
            heapq.heappush(q, node)
            distance[chrToNumber(node)] = 0

    for i in range(52):
        if distance[i] != INF:
            if i < 26:
                if x != chr(i+65):
                    print(f"{x} => {chr(i+65)}")
            else:
                if x != chr(i+71):
                    print(f"{x} => {chr(i+71)}")


for i in range(65, 91):
    dijkstra(chr(i))
for i in range(97, 123):
    dijkstra(chr(i))
