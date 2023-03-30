import heapq

count = 1
while True:
    N = int(input())
    if N==0:
        break
    
    graph = []

    q = []

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    INF = int(1e9)

    for i in range(N):
        graph.append(list(map(int,input().split())))

    distance = [[INF for i in range(N)] for j in range(N)]
    distance[0][0] = graph[0][0]
    q.append((graph[0][0], 0,0)) #cost, row, col

    while q:
        cost, row, col = heapq.heappop(q)
        
        if distance[row][col] < cost:
            continue

        for i in range(4):
            next_row = row+dr[i]
            next_col = col+dc[i]

            if 0 <= next_row < N and 0 <= next_col < N:
                if distance[next_row][next_col] > cost + graph[next_row][next_col]:
                    distance[next_row][next_col] = cost + graph[next_row][next_col]
                    heapq.heappush(q,(distance[next_row][next_col],next_row,next_col))

    print(f"Problem {count}: {distance[N-1][N-1]}")
    count+=1