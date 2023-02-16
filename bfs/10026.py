from collections import deque

N = int(input())
graph = []
visited = [[0]*N for _ in range(N)]
count1 = 0
count2 = 0
print(visited)

for _ in range(N):
    graph.append(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

q = deque()

for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            q.append((r,c,graph[r][c]))

            while(q):
                row, col, color = q.popleft()
                visited[row][col] = 1

                for i in range(4):
                    nr = row+dr[i]
                    nc = col+dc[i]
                    if (0>nr or 0>nc or N<=nr or N<=nc):
                        continue
                    if (visited[nr][nc]==1):
                        continue
                    if (graph[nr][nc] is not color):
                        continue
                    
                    q.append((nr,nc,color))

            count1+=1

for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            q.append((r,c,graph[r][c]))

            while(q):
                row, col, color = q.popleft()
                visited[row][col] = 1

                for i in range(4):
                    nr = row+dr[i]
                    nc = col+dc[i]
                    if (0>nr or 0>nc or N<=nr or N<=nc):
                        continue
                    if (visited[nr][nc]==1):
                        continue
                    if color is ('R' or 'G'):
                        if (graph[nr][nc] == 'B'):
                            continue
                    else:
                        if (graph[nr][nc] is not color):
                            continue
                    q.append((nr,nc,color))

            count2+=1
print(count1,count2)
                
    
