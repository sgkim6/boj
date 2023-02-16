import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

arr = []
tree = [0]*(n*4)

for _ in range(n):
    arr.append(int(input()))

def init(node,start,end):
    

