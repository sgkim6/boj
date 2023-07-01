N, M = map(int, input().split())

arr = []
parent = [x for x in range(N)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


flag = False

for i in range(1, M+1):
    a, b = map(int, input().split())
    arr.append((a, b))
for i in range(1, M+1):
    if find(arr[i-1][0]) == find(arr[i-1][1]):
        print(i)
        flag = True
        break
    else:
        union(arr[i-1][0], arr[i-1][1])

if not flag:
    print(0)
