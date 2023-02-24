from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
output = set()
for i in permutations(arr, m):
    output.add(i)

output = list(output)
output.sort()
for i in output:
    for c in i:
        print(c, end=' ')
    print()
