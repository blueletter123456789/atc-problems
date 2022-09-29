from collections import Counter

n = int(input())
p = Counter(list(map(int, input().split())))

ans = False
if len(p) == 1 and 0 in p:
  ans = True
elif len(p) == 2 and n % 3 == 0:
  if 0 in p and p[0] * 3 == n:
    ans = True
elif len(p) == 3 and n % 3 == 0:
  x = 0
  cnt = True
  for key, val in p.items():
    x = x ^ key
    cnt = cnt and (val*3 == n)
  if x == 0 and cnt:
    ans = True

if ans:
    print('Yes')
else:
    print('No')
