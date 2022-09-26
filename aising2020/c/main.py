n = int(input())

ans = [0]*(n+1)
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            c = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if c > n:
                break
            ans[c] += 1

for i in range(1, n+1):
    print(ans[i])
