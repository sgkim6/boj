N, M = map(int, input().split())

trains = [0 for i in range(N+1)]

for i in range(M):
    tmp = input().split()
    cmd = int(tmp[0])
    if cmd == 1 or cmd == 2:
        i = int(tmp[1])
        x = int(tmp[2])

        if cmd == 1:
            trains[i] = trains[i] | (1 << x-1)
        elif cmd == 2:
            trains[i] = trains[i] & ~(1 << x-1)
    elif cmd == 3 or cmd == 4:
        i = int(tmp[1])
        if cmd == 3:
            trains[i] = (trains[i] << 1) & ((1 << 20)-1)
        elif cmd == 4:
            trains[i] = (trains[i] >> 1)

train_set = set(trains[1:])

print(len(train_set))
