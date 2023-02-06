import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for test_case in range(1,T+1):
    answer = 0
    dic = defaultdict(int)
    N = int(input())
    for _ in range(N-1):
        val, key = map(int,input().split())
        dic[key] = val
    A,B = map(int,input().split())

    A_parent = [A]
    B_parent = [B]
    B_start = dic[B]
    A_start = dic[A]
    while A_start != 0:
        A_parent.append(A_start)
        A_start = dic[A_start]
    while B_start != 0:
        B_parent.append(B_start)
        B_start = dic[B_start]
    
    # for i in range(min(len(A_parent),len(B_parent))):
    #     if A_parent[-i-1] == B_parent[-i-1]:
    #         answer = A_parent[-i-1]
    i,j = 0,0
    if len(A_parent)>len(B_parent):
        i = len(A_parent) - len(B_parent)
    else:
        j = len(B_parent) - len(A_parent)
    
    while A_parent[i]!=B_parent[j]:
        i+=1
        j+=1
    print(A_parent[i])
    #print(answer)

