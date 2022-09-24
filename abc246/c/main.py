import heapq

n, k, x = map(int, input().split())
a = list()
for i in list(map(int, input().split())):
    a.append(-i)

total_amount = -sum(a)

heapq.heapify(a)
discount = 0
while len(a) and k > 0:
    amount = -heapq.heappop(a)
    if amount//x:
        ki = min(k, amount//x)
    else:
        ki = 1
    
    di = min(x * ki, amount)
    discount += di
    k -= ki
    if amount - di > 0:
        heapq.heappush(a, -(amount-di))

print(total_amount - discount)
