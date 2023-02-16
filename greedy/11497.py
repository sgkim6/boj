import sys,math
input = sys.stdin.readline


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    tmp = []

    for i in range(0,len(arr),2):
        tmp.append(arr[i])
    if len(arr)%2 == 1:
        for i in range(2,len(arr)+1,2):
            tmp.append(arr[-i])
    else:
        for i in range(1,len(arr)+1,2):
            tmp.append(arr[-i])
    
    
    
    level = abs(tmp[0]-tmp[-1])
    for i in range(len(tmp)):
        level = max(abs(tmp[i]-tmp[i-1]) , level)
    print(level)
