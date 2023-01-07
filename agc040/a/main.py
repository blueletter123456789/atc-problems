s = input()
n = len(s) + 1
a = [0] * n

for i in range(n-1):
    if s[i] == '<':
        if a[i+1] < a[i]+1:
            a[i+1] = a[i] + 1

for i in range(2, n+1):
    idx = n - i
    if s[idx] == '>':
        if a[idx] < a[idx+1]+1:
            a[idx] = a[idx+1] + 1

print(sum(a))
