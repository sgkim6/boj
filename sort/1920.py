N = int(input())
s = set(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))
for i in target:
    if i in s:
        print(1)
    else:
        print(0)