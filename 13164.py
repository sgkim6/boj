import heapq

N, K = map(int, input().split())

childrens = list(map(int, input().split()))

diff_list = []

for i in range(len(childrens)-1):
    heapq.heappush(diff_list, -(childrens[i+1] - childrens[i]))

for i in range(K-1):
    heapq.heappop(diff_list)

print(-sum(diff_list))
