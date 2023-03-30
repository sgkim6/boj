N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

INF = int(2e9)

dp = [[INF for i in range(1<<N)] for j in range(N)]

