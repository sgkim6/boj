import re

N = input()

L1 = []
L2 = []

Left = N.split('-', 1)[0]
Right = []

if '-' in N:
    Right = N.split('-', 1)[1]

L1 = Left.split('+')
if '-' in N:
    L2 = re.split(r'[^0-9]', Right)

L1 = list(map(int, L1))
L2 = list(map(int, L2))

print(sum(L1)-sum(L2))
