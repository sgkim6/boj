import sys

N, M = map(int,input().split())

parent = [x for x in range(N+1)]
answer = set()

def find(x):
    if parent[x]!=x:
        return find(parent[x])
    else:
        return parent[x]

def union(x,y):
    global parent
    x = find(x)
    y = find(y)
    if x>y:
        parent[x] = y
    else:
        parent[y] = x

for _ in range(M):
    a, b = map(int,input().split())
    union(a,b)

for i in parent[1:]:
    answer.add(find(i))
print(len(answer))

