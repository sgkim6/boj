def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
