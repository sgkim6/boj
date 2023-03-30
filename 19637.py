<<<<<<< HEAD
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
=======
N, M = map(int,input().split())

for _ in range(N):
    
>>>>>>> e70783d44df237dacb1c3267529371b9aebe9c9d
