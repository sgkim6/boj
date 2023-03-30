from collections import defaultdict

N, M, K1, K2 = map(int,input().split())

graph1 = defaultdict(list)
graph2 = defaultdict(list)

answer1 = 0
answer2 = 0

for i in range(K1):
    player, pick = map(int,input().split())
    graph1[player].append(pick)

for i in range(K2):
    player, pick = map(int,input().split())
    graph2[player].append(pick)

selected1 = [-1] * (M+1)
selected2 = [-1] * (M+1)

def dfs(x):
    global visited1
    if visited1[x]:
        return False
    
    visited1[x] = True

    for target in graph1[x]:
        if selected1[target] == -1 or dfs(selected1[target]): #픽이 가능하거나 선픽한애가 양보 가능하면
            selected1[target] = x
            return True

    return False

def dfs2(x):
    global visited2
    if visited2[x]:
        return False
    
    visited2[x] = True

    for target in graph2[x]:
        if selected2[target] == -1 or dfs2(selected2[target]): #픽이 가능하거나 선픽한애가 양보 가능하면
            selected2[target] = x
            return True

    return False

for i in range(1,N+1):
    visited1 = [False] * (N+1)
    dfs(i)

for i in selected1:
    if i>0:
        answer1+=1

for i in range(1,N+1):
    visited2 = [False] * (N+1)
    dfs2(i)

for i in selected2:
    if i>0:
        answer2+=1
print("네 다음 힐딱이" if answer1<answer2 else "그만 알아보자")