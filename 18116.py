from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())

dic = defaultdict(int)  # key : 부품, value : 로봇의 크기(부품갯수)
parents = []

for i in range(0, 10**6+1):  # init
    parents.append(i)
    dic[i] = 1


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:  # 같은 로봇에 속할 경우 합치면 안됨
        return
    if x < y:
        parents[y] = x
        dic[x] += dic[y]  # union 하면서 부모 부품에 현재 크기 저장(자식은 관여x)
    else:
        parents[x] = y
        dic[y] += dic[x]


for _ in range(N):
    tmp = input().split()
    cmd = tmp[0]
    first = int(tmp[1])
    second = int(tmp[-1])

    if cmd == 'I':
        union(first, second)
    elif cmd == 'Q':
        print(dic[find(first)])
