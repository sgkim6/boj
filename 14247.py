n = int(input())

multi = n-1

answer = 0

first = list(map(int, input().split()))

growth = list(map(int, input().split()))

trees = []


for tree in zip(growth, first):
    trees.append(tree)

trees.sort(reverse=True)

l = len(trees)

for i in range(n):
    if i == l:
        break
    answer = answer + trees[i][1] + trees[i][0] * multi
    multi -= 1
    if multi == -1:
        break

print(answer)
