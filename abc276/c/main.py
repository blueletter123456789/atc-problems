n = int(input())
p = list(map(int, input().split()))

change_idx = 0
for i in range(n-1):
    if p[i] > p[i+1]:
        change_idx = i

tgt_idx = change_idx+1
for p_idx in range(change_idx+1, n):
    if p[change_idx] > p[p_idx] and p[tgt_idx] < p[p_idx]:
        tgt_idx = p_idx

p[change_idx], p[tgt_idx] = p[tgt_idx], p[change_idx]
ans = p[:change_idx+1] + sorted(p[change_idx+1:], reverse=True)

print(' '.join(list(map(str, ans))))
