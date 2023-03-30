import sys
input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = 1
INF = int(1e9)

dp = [[-1 for i in range(1 << N)] for _ in range(N)]


def tsp(node, visited):
    if visited == (1 << N)-1:
        if graph[node][0]:
            return graph[node][0]
        else:
            return INF
        
    if dp[node][visited] != -1:
        return dp[node][visited]

    min_dist = INF
    for i in range(1,N):
        if graph[node][i] == 0:
            continue
        if (visited & 1<<i):
            continue
            
        min_dist = min(min_dist, tsp(i,visited | (1<<i)) + graph[node][i])
    
    dp[node][visited] = min_dist
    
    return min_dist

print(tsp(0,1))