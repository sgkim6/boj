import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    answer = 0
    while (len(arr) > 1):
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        s = a+b
        heapq.heappush(arr, s)
        answer += s
    print(answer)
