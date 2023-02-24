import heapq
N = int(input())
heap = []
answer = 0
for _ in range(N):
    heapq.heappush(heap, int(input()))
while len(heap) > 1:
    tmp1 = heapq.heappop(heap)
    tmp2 = heapq.heappop(heap)
    answer += (tmp1+tmp2)
    heapq.heappush(heap, (tmp1+tmp2))

print(answer)
