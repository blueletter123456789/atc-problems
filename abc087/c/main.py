n = int(input())

A = [list(map(int, input().split())) for _ in range(2)]

ans = 0
for i in range(n):
    sum_num = 0
    flg = 0
    for j in range(n):
        if i == j:
            sum_num += A[flg][j]
            flg = 1
        sum_num += A[flg][j]

    ans = max(ans, sum_num)

print(ans)
