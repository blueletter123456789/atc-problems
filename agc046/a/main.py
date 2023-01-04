x = int(input())

for k in range(1, 361):
    if ((k * x) % 360) == 0:
        break

print(k)
