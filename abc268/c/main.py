n = int(input())
p = list(map(int, input().split()))
sum_num = [0]*n
for i, num in enumerate(p):
    d = (num - i) % n
    sum_num[d] += 1

ans = 0
for i in range(n):
    ans = max(ans, 
            sum_num[i]+sum_num[(i-1)%n]+sum_num[(i+1)%n])

print(ans)
