M = 998244353

n = int(input())

a = [int(i) for i in input()]
b = [int(i) for i in input()]

for i in range(n):
    if a[i] > b[i]:
        a[i], b[i] = b[i], a[i]

min_num = max_num = 0
for a_num, b_num in zip(a, b):
    min_num *= 10
    max_num *= 10
    min_num += a_num
    max_num += b_num
    min_num %= M
    max_num %= M

print((min_num * max_num) % M)
