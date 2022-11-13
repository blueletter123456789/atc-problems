import bisect


def is_trinagle(a, b, c):
    return all([a < b + c, b < c + a, c < a + b])


n = int(input())
L = list(map(int, input().split()))
L.sort()

cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        idx = bisect.bisect_left(L, L[i] + L[j]) - 1
        if is_trinagle(L[i], L[j], L[idx]):
            cnt += max(0, idx - j)
print(cnt)
