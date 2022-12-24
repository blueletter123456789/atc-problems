class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


n, q = map(int, input().split())
s = input()
bit_tree = Bit(n)
for idx, char in enumerate(s[1:]):
    if char == 'C' and s[idx] == 'A':
        bit_tree.add(idx+2, 1)

for _ in range(q):
    l, r = map(int, input().split())
    ans = bit_tree.sum(r) - bit_tree.sum(l)
    print(ans)

# 累積和を使用すればO(1)で計算することができる
