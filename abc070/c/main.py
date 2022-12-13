def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
T = [int(input()) for _ in range(n)]

ans = 1
for i in T:
    ans = ans // gcd(ans, i)
    ans *= i

print(ans)
