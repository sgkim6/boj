import sys
sys.setrecursionlimit(10**7)

N = int(input())
arr = list(map(int,input().split()))
K = int(input())

def sort(left,right,depth):
    global arr
    
    depth = depth//2
    
    if (right-left) == 1:
        tmp_l = arr[left]
        tmp_r = arr[right]
        arr[left] = min(tmp_l,tmp_r)
        arr[right] = max(tmp_l,tmp_r)
        return
    else:
        sort(left,left+(right-left)//2,depth)
        sort(left+(right-left)//2+1,right,depth)

    # if depth == K:
    #     return
    
sort(0,7,N/2)
print(arr)