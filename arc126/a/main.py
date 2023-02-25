t = int(input())

for _ in range(t):
    n_1, n_3, n_2 = map(int, input().split())
    n_3 //= 2
    cnt = 0
    cnt = min(n_2, n_3)
    n_2 -= cnt
    n_3 -= cnt

    tmp_num = min(n_3, n_1 // 2)
    cnt += tmp_num
    n_1 -= tmp_num * 2
    n_3 -= tmp_num

    tmp_num = min(n_2 // 2, n_1)
    cnt += tmp_num
    n_1 -= tmp_num
    n_2 -= tmp_num * 2

    tmp_num = min(n_2, n_1 // 3)
    cnt += tmp_num
    n_1 -= tmp_num * 3
    n_2 -= tmp_num

    cnt += n_1 // 5

    print(cnt)
