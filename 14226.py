from collections import deque

N = int(input())

visited = [False * (N+1)]

visited = set()
visited.add((1, 1))
q = deque()

q.append((1, 1, 1))  # 현재 수, 저장된 수, 시간

while q:
    cur, stored, time = q.popleft()
    if cur == N:
        print(time)
        break
    # 1
    if (cur, cur) not in visited:
        q.append((cur, cur, time+1))
        visited.add((cur, cur))

    # 2
    if (cur + stored, stored) not in visited:
        q.append((cur + stored, stored, time+1))
        visited.add((cur + stored, stored))

    # 3
    if cur <= 0:
        continue
    if (cur-1, stored) in visited:
        continue
    q.append((cur-1, stored, time+1))
    visited.add((cur-1, stored))
