class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visit = [False] * n

        res = 0
        def dfs(i):
            if not adj[i] or visit[i] == True:
                return
            visit[i] = True
            for j in adj[i]:
                dfs(j)

        for k in range(n):
            if visit[k] == False:
                dfs(k)
                res += 1
        
        return res