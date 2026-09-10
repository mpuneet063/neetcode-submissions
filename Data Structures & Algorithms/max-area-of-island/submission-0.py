class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = []
        maxArea = 0
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            islands = []
            area = 0
            while q:
                row,col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                island = []
                for dr, dc in directions:
                    r,c = row, col
                    
                    if ((r+dr) in range(rows) and
                        (c+dc) in range(cols) and
                        grid[r+dr][c+dc] == 1 and 
                        (r+dr, c+dc) not in visit):

                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
                        island.append((r+dr,c+dc))

                islands.append(island)
                area = max(area, len(islands))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, bfs(r,c))

        return maxArea