def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
a = list(map(int, input().split()))

gcd_num = 0
for num in a:
    gcd_num = gcd(num, gcd_num)

cnt = 0
for i in a:
    tgt_num = i // gcd_num
    while tgt_num % 2 == 0:
        tgt_num //= 2
        cnt += 1

    while tgt_num % 3 == 0:
        tgt_num //= 3
        cnt += 1

    if tgt_num != 1:
        cnt = -1
        break

print(cnt)
