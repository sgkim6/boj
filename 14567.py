from collections import deque, defaultdict

N, M = map(int, input().split())

in_degree = [0 for i in range(N+1)]
answer = [0 for i in range(N+1)]

graph = defaultdict(list) #간선 정보 저장
q = deque() #bfs

for _ in range(M): #초기 in_degree 세팅
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

for i in range(1, N+1): #시작 노트 세팅
    if in_degree[i] == 0:
        q.append(i)
        answer[i] = 1

while q: #bfs
    current_node = q.popleft()
    for target in graph[current_node]:
        in_degree[target] -= 1
        if in_degree[target] == 0:
            answer[target] = answer[current_node] + 1
            q.append(target)

print(*answer[1:])
