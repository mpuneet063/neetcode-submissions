class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n
    
    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu     # u should always be > v
        self.parent[pv] = pu    # make u parent of v
        self.rank[pu] += self.rank[pv]  # increase rank of pu
        self.count -= 1     # successfully merged two components
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factor_index = {}   # f -> index of value with factor f
        for i , n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while n % f == 0:
                        n //= f
                f += 1
            
            if n > 1:
                if n in factor_index:
                    uf.union(i,factor_index[n])
                else:
                    factor_index[n] = i
            
        return uf.count == 1