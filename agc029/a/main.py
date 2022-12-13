class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += (i & -i)


input_s = [1 if i == 'B' else 0 for i in input()]
bit_ins = BIT(len(input_s))
ans = 0
for idx, si in enumerate(input_s):
    ans += (idx - bit_ins.sum(si+1))
    bit_ins.add(si+1, 1)

print(ans)
