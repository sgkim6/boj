import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewel = []
bag = []
stored_jewel = []
answer = 0

for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewel, (m, v))

for _ in range(K):
    heapq.heappush(bag, int(input()))

while bag:
    cur_bag = heapq.heappop(bag)
    while jewel:
        if jewel[0][0] <= cur_bag:
            tmp = heapq.heappop(jewel)
            heapq.heappush(stored_jewel, (-tmp[1], tmp[0]))
        else:
            break

    if stored_jewel:
        answer -= heapq.heappop(stored_jewel)[0]


print(answer)
