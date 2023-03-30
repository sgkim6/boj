N = int(input())

next_nodes = [0]

answer = []

visited = [False] * (N+1)

for i in range(1,N+1):
    next_nodes.append(int(input()))

for i in range(1,N+1):
    tmp = []
    
    start_node = i
    cur_node = i

    while True:
        
        next_node = next_nodes[cur_node]

        if next_node in tmp:
            break

        tmp.append(next_node)

        if cur_node == next_node:
            answer.extend(tmp)
            
            break

        if visited[next_node] == True:
            break

        if next_node == start_node: #원래 위치로 돌아오면
            answer.extend(tmp)
            break

        cur_node = next_node

    visited[i] = True

print(len(answer))
for i in sorted(answer):
    print(i)