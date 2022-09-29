from collections import defaultdict

n, m = map(int, input().split())

ac = defaultdict(int)
wa = defaultdict(int)
for _ in range(m):
    p, s = input().split()
    if s == 'AC':
        ac[p] += 1
    else:
        if p not in ac:
            wa[p] += 1

ans_wa = 0
for key in ac:
    ans_wa += wa.get(key, 0)
print(len(ac), ans_wa)
