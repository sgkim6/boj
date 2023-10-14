n, k = map(int, input().split())

lst = list(map(int, input().split()))

length = sum(lst)

lst += reversed(lst)

result = 0
i = 0
flag = 0

for ls in lst:
    result += 1
    i += ls
    if i > k:
        flag = 1
        break

print(result if k < length else 2*n+1 - result)
# l1 = result % len(lst)

# print(lst[l1-1])
