import sys
from collections import deque, defaultdict

N = int(input())

graph = defaultdict(list)

times = [0 for i in range(N+1)]  # 해당 건물을 짓는데 걸리는 총 시간(answer)

req_times = [0 for i in range(N+1)]  # 해당 건물 건설 전까지 걸리는 시간

in_degree = [0 for i in range(N+1)]  # 진입 차수

for i in range(1, N+1):  # 초기값 세팅
    cmd = input().split()
    times[i] = int(cmd[0])
    for j in cmd[1:-1]:
        graph[int(j)].append(i)
        in_degree[i] += 1

q = deque()

for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    for target in graph[tmp]:
        req_times[target] = max(req_times[target], times[tmp])
        in_degree[target] -= 1
        if in_degree[target] == 0:
            times[target] += req_times[target]
            q.append(target)

for i in times[1:]:
    print(i)
