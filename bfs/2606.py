import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
E = int(input())

parent = [i for i in range(N+1)]

for _ in range(E):
    start, end = map(int, input().split())
    union(parent, start, end)

answer = 0

for i in range(1, N+1):
    if find(parent, parent[i]) == 1:
        answer += 1

print(answer-1)


# q = deque()
# visited = [0]*(N+1)
# q.append(1)
# visited[1] = 1

# while q:
#     start = q.popleft()
#     for i in graph[start]:
#         if visited[i] == 0:
#             visited[i] = 1
#             q.append(i)

# print(visited.count(1)-1)
