N = int(input())

N = N*2

i = 1
while True:
    if i*(i+1) <= N < (i+1)*(i+2):
        print(i)
        break
    i += 1
