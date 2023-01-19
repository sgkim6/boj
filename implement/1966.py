from collections import deque
import heapq

tc = int(input())

for i in range(tc):
    q = deque()

    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    answer = []
    idx = list(range(N))
    idx_q = deque()
    idx_q.extend(idx)
    q.extend(L)
    max_heap = []
    for item in L:
        heapq.heappush(max_heap, (-item, item))

    while q:
        item = q.popleft()
        if item == max_heap[0][1]:
            heapq.heappop(max_heap)
            answer.append(idx_q.popleft())
        else:
            q.append(item)
            idx_q.rotate(-1)

    result = answer.index(M)+1
    print(result)
