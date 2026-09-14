class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is valid if it has no cycles and is fully connected
        if len(edges) > n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
  
        q = deque()
        q.append([0, -1])
        visit = set()
        visit.add(0)
        while q:
            node, parent = q.popleft()
            for a in adj[node]:
                if a == parent:
                    continue
                if a in visit:
                    return False
                visit.add(a)
                q.append((a,node))

        return len(visit) == n