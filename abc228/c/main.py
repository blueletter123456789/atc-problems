n, k = map(int, input().split())
p = []
for i in range(n):
    p.append((sum(map(int, input().split())), i))

p.sort(reverse=True)
ans = ["No"] * n
last_score = 0
for rank, (score, idx) in enumerate(p):
    if rank < k:
        ans[idx] = "Yes"
        last_score = score
    elif score + 300 >= last_score:
        ans[idx] = "Yes"
    else:
        break

print("\n".join(ans))
