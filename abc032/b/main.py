s = input()
k = int(input())

seen = set()
for i in range(len(s)-k+1):
    if s[i:i+k] not in seen:
        seen.add(s[i:i+k])

print(len(seen))
