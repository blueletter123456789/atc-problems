from collections import defaultdict

n = int(input())

seen = defaultdict(int)
limit_n = int(n ** 0.5)
for i in range(1, limit_n+1):
    seen[i*i] += 1
    for j in range(i+1, n//i + 1):
        seen[i*j] += 2

cnt = 0
for c in range(1, n):
    cnt += seen[n-c]

print(cnt)

# (n-1)//aで全探索を行えばよい
