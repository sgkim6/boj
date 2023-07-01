import heapq
import math

N = int(input())

q = []

amount = 0

for i in range(N):
    x, a = map(int, input().split())
    amount += a
    heapq.heappush(q, (x, a))

center = amount // 2 + amount % 2

while center > 0:
    position, population = heapq.heappop(q)
    center -= population
    if center <= 0:
        print(position)
        break
