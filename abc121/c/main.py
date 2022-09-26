n, m = map(int, input().split())
stores = list()
for _ in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])

stores.sort()
amount = 0
i = 0
while m > 0:
    a, b = stores[i]
    if b > m:
        amount += a * m
        m -= m
    else:
        amount += a * b
        m -= b
    i += 1

print(amount)
