class UnionFind(object):
    def __init__(self, len_uni):
        self.par = [-1 for _ in range(len_uni)]
        self.size = [1 for _ in range(len_uni)]

    def root(self, a):
        if self.par[a] == -1:
            return a
        self.par[a] = self.root(self.par[a])
        return self.par[a]

    def is_same(self, a, b):
        return self.root(a) == self.root(b)

    def unite(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        if self.uni_size(a) < self.uni_size(b):
            a, b = b, a
        self.par[b] = a
        self.size[a] += self.size[b]
        return True

    def uni_size(self, a):
        return self.size[self.root(a)]


n, m = map(int, input().split())
un = UnionFind(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    un.unite(a, b)

cnt = 0
for i in range(n):
    if i+1 == un.root(i+1):
        cnt += 1

print(cnt - 1)
