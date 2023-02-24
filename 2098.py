N = int(input())

graph = []

for _ in range(N):
    graph.append(map(int, input().split()))

visited = 1
INF = 999999999

dp = [[INF for i in range((1 << N))] for _ in range(N)]


def tsp(node, visited):
    if visited == (1 << N)-1:
        return graph[node][0]
    if dp[node][visited] != INF:
        return dp[node][visited]
