import heapq
import sys

input = sys.stdin.readline

N = int(input())

q1 = []

lst = []

answer = 0
last_time = 0

for i in range(N):
    start_time, end_time = map(int, input().split())
    heapq.heappush(lst, (start_time, end_time))
while lst:
    start_time, end_time = heapq.heappop(lst)
    if len(q1) == 0:
        heapq.heappush(q1, (end_time, start_time))  # 끝시간, 처음시간
    else:
        if q1[0][0] <= start_time:
            heapq.heappop(q1)
            heapq.heappush(q1, (end_time, start_time))
        else:
            heapq.heappush(q1, (end_time, start_time))

print(len(q1))
