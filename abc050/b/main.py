n = int(input())
T = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    ans = 0
    p, x = map(int, input().split())
    p -= 1
    for idx, t in enumerate(T):
        if idx == p:
            ans += x
            continue
        ans += t
    print(ans)
