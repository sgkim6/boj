from collections import deque
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
heap = []  # 가능한 강의 중 제일 비싼 강의를 저장
answer = 0
day = 0

for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(arr, (-d, -p))

if arr:
    day = -min(arr)[0]

while day > 0:
    while arr:
        if (-arr[0][0] == day):
            tmp = heapq.heappop(arr)
            heapq.heappush(heap, (tmp[1], tmp[0]))
        else:
            break

    if heap:
        answer -= heapq.heappop(heap)[0]
    day -= 1

print(answer)
