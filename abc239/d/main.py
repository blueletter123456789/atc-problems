a, b, c, d = map(int, input().split())

prime = [False, False]
for i in range(2, 201):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    prime.append(is_prime)

ans = False
for i in range(a, b+1):
    is_prime = False
    for j in range(c, d+1):
        if prime[i+j]:
            is_prime = True
            break
    if not is_prime:
        ans = True
        break

print("Takahashi" if ans else "Aoki")
