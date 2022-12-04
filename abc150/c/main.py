import itertools

n = int(input())
p = ''.join(list(input().split()))
q = ''.join(list(input().split()))

a = -1
b = -1
for idx, permutation in enumerate(itertools.permutations(range(1, n+1))):
    x = ''.join([str(num) for num in permutation])
    if x == p:
        a = idx
    if x == q:
        b = idx
    if a > 0 and b > 0:
        break

print(abs(a - b))
