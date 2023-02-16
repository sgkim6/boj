import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

parent = [i for i in range(0, n+1)]


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


def check(x, y):
    if find(x) != find(y):
        return False
    else:
        return True


for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        print("YES") if check(a, b) else print("NO")
