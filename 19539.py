N = int(input())

heights = list(map(int, input().split()))

remain = 0
use = 0

for i in heights:
    d, m = divmod(i, 2)
    remain += m
    use += d

if remain > use:
    print("NO")
else:
    if (use - remain) % 3 == 0:
        print("YES")
    else:
        print("NO")
