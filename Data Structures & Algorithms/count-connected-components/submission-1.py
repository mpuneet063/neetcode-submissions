class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
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
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # start with each node as its own component and join (Union)
        res = n
        dsu = DSU(n)

        for u, v in edges:
            if dsu.union(u,v):
                res -= 1

        return res
