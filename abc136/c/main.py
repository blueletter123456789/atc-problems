n = int(input())
h = list(map(int, input().split()))

is_increase = True
prev = -float('inf')
for i in h:
    if i < prev:
        is_increase = False
        break
    prev = i - 1 if prev < i else i

print('Yes' if is_increase else 'No')
