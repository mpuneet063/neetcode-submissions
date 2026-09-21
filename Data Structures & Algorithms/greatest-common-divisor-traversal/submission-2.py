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
        
        def factorize(num):
            factors = []
            factors.append(1)
            while num % 2 == 0:
                if 2 not in factors:
                    factors.append(2)
                num //= 2

            d = 3
            while d * d <= num:
                while num % d == 0:
                    if d not in factors:
                        factors.append(d)
                    num //= d
                d += 2

            if num > 1 :
                factors.append(num)
            
            return factors

        factors = []
        for n in nums:
            factors.append(factorize(n))

        highest = max(num for sub in factors for num in sub)
        adj = defaultdict(list)
        for i in range(2,highest+1):
            for f in range(len(factors)):
                if i in factors[f]:
                    adj[i].append(f)

        uf = UnionFind(len(nums))
        for nodes in adj.values():
            first = nodes[0]
            for rest in nodes[1:]:
                uf.union(first, rest)

        res = uf.count

        return res == 1