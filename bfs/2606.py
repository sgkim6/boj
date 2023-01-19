from collections import defaultdict, deque

N = int(input())
l = int(input())

dic = defaultdict(list)


for _ in range(l):
    start, end = map(int, input().split())
    dic[start].append(end)
    dic[end].append(start)

q = deque()
visited = [0]*(N+1)
q.append(1)
visited[1] = 1

while q:
    start = q.popleft()
    for i in dic[start]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)

print(visited.count(1)-1)
