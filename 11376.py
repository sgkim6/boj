import sys
from collections import defaultdict
sys.setrecursionlimit(100000)


N, M = map(int,input().split())

graph = defaultdict(list)

selected = [-1 for _ in range(M+1)] #idx = 일 , value = 담당 직원

for i in range(1,N+1):     
    tmp = input().split()
    if len(tmp) > 1:
        for task in tmp[1:]:
            graph[i].append(int(task))

def dfs(x):
    global visited
    if visited[x]:
        return False
    
    visited[x] = True
    
    for target in graph[x]:
        if selected[target]==-1 or dfs(selected[target]):
            selected[target] = x 
            return True

    return False

for i in range(1,N+1):
    visited = [False for _ in range(N+1)]
    dfs(i)
    visited = [False for _ in range(N+1)]
    dfs(i)

answer = 0
for i in selected:
    if i>0:
        answer += 1
print(answer)