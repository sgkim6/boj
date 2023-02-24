import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = []

answer = 0

for _ in range(N):
    no, start, end = map(int, input().split())
    arr.append((start, end))

arr.sort()

q = deque(arr)

while q:
    cur_class = q.popleft()
    end_time = cur_class[1]

    for _ in range(len(q)):
        if q[0][0] >= end_time:
            end_time = q.popleft()[1]
        else:
            q.append(q.popleft())

    answer += 1

print(answer)
# 시간 초과
