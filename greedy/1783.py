height, length = map(int,input().split())

if height<=1:
    print(1)
elif height == 2:
    print(min(1+(length-1)//2,4))
elif height>2:
    if length<=6:
        print(min(4,length))
    else:
        print(length-2)
