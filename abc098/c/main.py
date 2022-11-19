n = int(input())
s = input()

to_w = [0]*(n+1)
to_e = [0]*(n+1)

for idx, direction in enumerate(s):
    to_w[idx+1] = to_w[idx]
    to_e[idx+1] = to_e[idx]

    if direction == 'E':
        to_e[idx+1] += 1
    else:
        to_w[idx+1] += 1

ans = float('inf')
for i in range(1, n+1):
    cnt_w = to_w[i-1]
    cnt_e = to_e[n] - to_e[i]
    ans = min(ans, cnt_w + cnt_e)

print(ans)
