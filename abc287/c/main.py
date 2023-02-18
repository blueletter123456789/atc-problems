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


def main():
    n, m = map(int, input().split())
    if n - m != 1:
        return False

    uf = UnionFind(n)

    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
        uf.unite(u, v)

    one_cnt = two_cnt = 0
    for idx, e in enumerate(G):
        if len(e) == 1:
            one_cnt += 1
        elif len(e) == 2:
            two_cnt += 1
        else:
            return False

        if not uf.is_same(0, idx):
            return False

    return one_cnt == 2 and two_cnt == n - 2


if __name__ == '__main__':
    print('Yes' if main() else 'No')
