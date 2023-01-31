k = int(input())

cnt = 0
for a in range(1, k+1):
    for b in range(1, k//a+1):
        cnt += k//(a * b)

print(cnt)
