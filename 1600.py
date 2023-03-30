K = int(input())

col, row = map(int,input().split())

graph = []

for i in range(row):
    graph.append(list(map(int,input().split())))
