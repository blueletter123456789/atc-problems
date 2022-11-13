intput_lst = list(map(int, input().split()))

a, b, c = sorted(intput_lst)

cnt = 0
cnt += (c - a) // 2
cnt += (c - b) // 2

if a % 2 != b % 2:
    cnt += 2
elif a % 2 == b % 2 == c % 2:
    pass
else:
    cnt += 1

print(cnt)
