class UnionFind:
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dsu = UnionFind(n)
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda x: x[2])

        mst_weight = 0
        for u,v,w,i in edges:
            if dsu.union(u,v):
                mst_weight += w
        
        critical, pseudo = [], []

        for n1,n2,e_w,i in edges:
            # try without curr edge
            weight = 0
            uf = UnionFind(n)
            for u,v,w,j in edges:
                if i != j and uf.union(u,v):
                    weight += w
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue
    
            # try with curr edge
            uf = UnionFind(n)
            uf.union(n1,n2)
            weight = e_w
            for u,v,w,j in edges:
                if uf.union(u,v):
                    weight += w

            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]