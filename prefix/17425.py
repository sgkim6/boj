import sys
input = sys.stdin.readline
T = int(input())

prefix_sum = [0]

for i in range(1,1000001):
    tmp = 0
    prefix_sum.append(prefix_sum[i-1]+tmp)

# for test_case in range(1,T+1):
#     N = int(input())
#     answer = 0
#     for i in range(1,N+1):
#         answer += i*(N//i)
#     print(answer)