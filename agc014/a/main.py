a, b, c = map(int, input().split())

cnt = -1
for i in range(100):
    if a % 2 or b % 2 or c % 2:
        cnt = i
        break
    new_a = b // 2 + c // 2
    new_b = a // 2 + c // 2
    new_c = a // 2 + b // 2

    a, b, c = new_a, new_b, new_c

print(cnt)
