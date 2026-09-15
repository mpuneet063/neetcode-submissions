class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, visit):
            visit.add(node)
            depth = 0

            for a in adj[node]:
                if a not in visit:
                    depth = max(depth, 1 + dfs(a,visit))

            visit.remove(node)  # backtrack so other paths can visit this node
            return depth

        heights = []
        for i in range(n):
            h = dfs(i,set())
            heights.append(h)

        minHeight = min(heights)

        return [i for i, j in enumerate(heights) if j == minHeight]