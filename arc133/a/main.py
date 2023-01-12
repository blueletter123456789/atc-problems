n = int(input())

a = []
for num in list(map(int, input().split())):
    a.append(num)

max_num = a[-1]
for left, right in zip(a[:(n-1)], a[1:]):
    if left > right:
        max_num = left
        break

print(' '.join([str(i) for i in a if i != max_num]))
