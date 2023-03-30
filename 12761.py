from collections import deque
import sys

A, B, N, M = map(int, input().split())

visited = [False] * 100001
q = deque()
visited[N] = True
q.append((N, 0))  # (index, depth)


def move(idx, cmd):  # +1 -1 +A -A +B -B *A *B
    global A, B
    if cmd == 0:
        return idx+1
    if cmd == 1:
        return idx-1
    if cmd == 2:
        return idx + A
    if cmd == 3:
        return idx - A
    if cmd == 4:
        return idx+B
    if cmd == 5:
        return idx-B
    if cmd == 6:
        return idx * A
    if cmd == 7:
        return idx * B


while q and not visited[M]:
    index, depth = q.popleft()

    for i in range(8):
        next_index = move(index, i)
        if (next_index < 0 or next_index >= 100001):
            continue
        if (next_index == M):
            print(depth + 1)
            visited[next_index] = True
            break
        if (visited[next_index]):
            continue
        q.append((next_index, depth+1))
        visited[next_index] = True
