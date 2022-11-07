n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

times = [float('inf')]*n
for i in range(n*2+1):
    times[i % n] = min(t[i % n], times[(i-1) % n]+s[(i-1) % n])

for i in times:
    print(i)
