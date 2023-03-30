from collections import deque,defaultdict

N, K = map(int,input().split())

graph = []

answer = defaultdict(list)

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for _ in range(N):
    graph.append(list(map(int,input().split())))

S, X, Y = map(int,input().split())

row = X-1
col = Y-1
time = 0

q = deque()

q.append((row, col, time))

if graph[row][col] != 0:
    print(graph[row][col])
else:
    while q:
        row, col, time = q.popleft()
        if time == S:
            continue
        
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]

            if 0<=n_row<N and 0<=n_col<N:
                if graph[n_row][n_col] != 0:
                    answer[time+1].append(graph[n_row][n_col])
                else:
                    q.append((n_row,n_col,time+1))
        if len(answer.keys())>1:
            break



    if answer.keys():
        keymin = int(min(answer.keys()))
        print(min(answer[keymin]))
    else:
        print(0)
# if len(answer)>0:
#     print(answer[0][1])
# else:
#     print(0)