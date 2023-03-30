
G = int(input())

P = int(input())

g=[]
for i in range(P):
    g.append(int(input()))

parent = [i for i in range(G+1)]

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    
    return parent[x]


def union(x):
    x = find(x)
    if x == 0:
        return False
    
    y = find(x-1)

    parent[x] = y
    return True
answer = 0
for i in g:
    if union(i):
        answer += 1
    else:
        break

print(answer)