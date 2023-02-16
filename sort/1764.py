import sys
input = sys.stdin.readline


N,M = map(int,input().split())

s1 = set()
s2 = set()

for _ in range(N):
    s1.add(input()[:-1])
for _ in range(M):
    s2.add(input()[:-1])

s3 = s1&s2

print(len(s3))
s3 = list(s3)
s3.sort()
for i in s3:
    print(i)