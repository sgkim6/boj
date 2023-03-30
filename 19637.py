from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

names = []
powers = []

for _ in range(N):
    name, power = input().split()
    power = int(power)
    names.append(name)
    powers.append(power)

for _ in range(M):
    input_power = int(input())
    print(names[bisect_left(powers, input_power)])
