import string

n = int(input())
chars = [{s: 0 for s in string.ascii_lowercase} for _ in range(n)]

for i in range(n):
    for s in input():
        chars[i][s] += 1

ans = ''
for s in string.ascii_lowercase:
    cnt = 51
    for i in range(n):
        cnt = min(cnt, chars[i][s])
    
    ans += s * cnt

print(ans)
