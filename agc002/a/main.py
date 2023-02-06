a, b = map(int, input().split())

ans = 'Zero'
if a > 0 or (a < 0 and b < 0 and (a - b) % 2):
    ans = 'Positive'
elif a < 0 and b < 0 and (a - b) % 2 == 0:
    ans = 'Negative'

print(ans)
