from collections import defaultdict

h, w = map(int, input().split())

s = [[''] * h for _ in range(w)]
t = [[''] * h for _ in range(w)]
for i in range(h):
    for j, char in enumerate(input()):
        s[j][i] = char

for i in range(h):
    for j, char in enumerate(input()):
        t[j][i] = char

pattern_s = defaultdict(int)
pattern_t = defaultdict(int)
for row_s, row_t in zip(s, t):
    pattern_s[''.join(row_s)] += 1
    pattern_t[''.join(row_t)] += 1

is_same = True
for key, val in pattern_s.items():
    if pattern_t[key] != val:
        is_same = False
        break

print('Yes' if is_same else 'No')
