class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 - 1
        rows , cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        
        def addcell(r,c):
            if (r<0 or c<0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == -1):
                return

            visit.add((r,c))
            q.append([r,c])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])


        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            dist += 1