from collections import deque

N, M = map(int, input().split())

arr = list(map(int, input().split()))

q = deque()

answer = 0

for i in range(1, N+1):
    q.append(i)

for i in arr:
    idx = q.index(i)
    if idx <= len(q)//2:
        q.rotate(-idx)
        answer += idx
        q.popleft()
    else:
        q.rotate(len(q)-idx)
        answer += len(q)-idx
        q.popleft()

print(answer)
