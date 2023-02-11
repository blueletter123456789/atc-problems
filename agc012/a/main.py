n = int(input())
a = list(map(int, input().split()))

a.sort()
print(sum(a[i] for i in range(n, n*3, 2)))
