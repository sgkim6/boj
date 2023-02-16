import sys, heapq
input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    cmd = int(input())
    if cmd==0:
        print(-heapq.heappop(q)) if q else print(0)
    else:
        heapq.heappush(q,-cmd)
