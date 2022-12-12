n = int(input())

a = b = -1
for i in range(50):
    for j in range(50):
        if (3 ** i + 5 ** j) == n:
            a, b = i, j
            break

if a > 0 and b > 0:
    print(a, b)
else:
    print(-1)
