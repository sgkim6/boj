import heapq
import sys


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


input = sys.stdin.readline

N = int(input())

heap = []
answer = 0
planets = []

parent = [i for i in range(N)]

for no in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, no))

planets.sort(key=lambda x: x[0])
for i in range(N-1):
    x_diff = planets[i+1][0] - planets[i][0]
    heapq.heappush(heap, (x_diff, planets[i][3], planets[i+1][3]))

planets.sort(key=lambda x: x[1])
for i in range(N-1):
    y_diff = planets[i+1][1] - planets[i][1]
    heapq.heappush(heap, (y_diff, planets[i][3], planets[i+1][3]))

planets.sort(key=lambda x: x[2])
for i in range(N-1):
    z_diff = planets[i+1][2] - planets[i][2]
    heapq.heappush(heap, (z_diff, planets[i][3], planets[i+1][3]))

while heap:
    tmp = heapq.heappop(heap)
    if find(tmp[1]) != find(tmp[2]):
        union(tmp[1], tmp[2])
        answer += tmp[0]
print(answer)
