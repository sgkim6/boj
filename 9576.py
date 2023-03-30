T = int(input())

for test_case in range(1,T+1):
    graph = [(0,0)]
    N, M = map(int,input().split())
    for i in range(M):
        graph.append(tuple(map(int,input().split())))
    
    selected = [-1] * (N+1)

    def dfs(x):
        global visited
        if visited[x]:
            return False
        
        visited[x] = True

        for target in range(graph[x][0],graph[x][1]+1):
            if selected[target] == -1 or dfs(selected[target]):
                selected[target] = x
                return True

        return False

    for i in range(1,M+1):
        visited = [False] * (M+1)
        dfs(i)
    
    answer = 0
    for i in selected:
        if i>0:
            answer+=1
    print(answer)
