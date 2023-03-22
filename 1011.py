T = int(input())

for test_case in range(1,T+1):
    x, y = map(int,input().split())
    gap = y - x 
    if gap == 1:
        print(1)
    else:
        for i in range(1,2**16):
            if i**2 < gap <= i*(i+1):
                print(2*i)
                break
            elif i*(i-1) < gap <= i**2:
                print(2*i-1)
                break