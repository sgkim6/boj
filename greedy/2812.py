from collections import deque

N, K = map(int,input().split())

q = deque(input())
answer = deque()

while(q):
    if len(answer) == 0:
        answer.append(q.popleft)

