N,M = map(int,input().split())
arr = []

depth = 0

def dfs(depth):
    tmp = []
    if depth==N:
        return
    
