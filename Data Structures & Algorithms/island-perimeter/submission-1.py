class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # use dfs
        visit = set()
        
        def dfs(i,j):
            if i >= m or j >= n or i<0 or j <0 or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0

            visit.add((i,j))
            res = dfs(i-1, j)
            res += dfs(i+1, j)
            res += dfs(i, j-1)
            res += dfs(i, j+1)
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i,j)