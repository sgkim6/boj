import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N, M = map(int, input().split())

dots = list(map(int, input().split()))

dots.sort()

for i in range(M):
    a, b = map(int, input().split())
    start_idx = bisect_left(dots, a)
    end_idx = bisect_right(dots, b)
    print(end_idx - start_idx)
