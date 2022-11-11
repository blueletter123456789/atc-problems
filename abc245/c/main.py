n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n)]
dp[0][0], dp[0][1] = min(A[0], B[0]), max(A[0], B[0])

flg = True
for idx, (a, b) in enumerate(zip(A[1:], B[1:])):
    min_num, max_num = float('inf'), 0
    for d in dp[idx]:
        if abs(d - a) <= k and min_num > a:
            min_num = a
        if abs(d - b) <= k and min_num > b:
            min_num = b
        if abs(d - a) <= k and max_num < a:
            max_num = a
        if abs(d - b) <= k and max_num < b:
            max_num = b
    if min_num == float('inf') and max_num == 0:
        flg = False
        break
    dp[idx+1][0], dp[idx+1][1] = min_num, max_num

print('Yes' if flg else 'No')
