from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
for _ in range(n):
    s = input()
    cnt[s] += 1

cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]))

que = [cnt[-1][0]]
for prev, tgt in zip(reversed(cnt), reversed(cnt[:-1])):
    if prev[1] != tgt[1]:
        break
    que.append(tgt[0])

print('\n'.join(reversed(que)))
