

c = int(input())

board = [[1], [2, 3, 4, 5, 2, 3], ]

counter = {1: 1, 2: 2, 3: 2, 4: 1, 5: 1}

querys = []

for i in range(c):
    n = int(input())
    querys.append(n)

for layer in range(2, 60):
    tmp_list = []
    for index in range(0, layer*6 + 1):
        used_set = set()
        if (index+1) % layer == 0:  # 꼭지점
            used_set.add(board[layer-1][((index+1) - (index+1)//layer)-1])
            used_set.add(board[layer][index-1])
            val = 0
            for i in range(1, 6):
                if i in used_set:
                    continue
                else:

        else:  # 모서리
            pass
