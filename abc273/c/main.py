import bisect


n = int(input())

A = list(map(int, input().split()))

sort_A = sorted(set(A))

ans = [0]*n
for i in A:
    idx = bisect.bisect_right(sort_A, i)
    ans[len(sort_A) - idx] += 1

for i in ans:
    print(i)
