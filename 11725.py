from collections import deque, defaultdict
import sys

input = sys.stdin.readline

graph = defaultdict(list)
N = int(input())

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()

