class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = deque()
        fresh = 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        def addcell(r,c, fresh):
            if (r in range(rows) and c in range(cols) and grid[r][c] == 1):
                grid[r][c] = 2
                q.append([r,c])
                return fresh - 1
            return fresh

        while fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                fresh = addcell(r-1,c, fresh)
                fresh = addcell(r+1,c, fresh)
                fresh = addcell(r,c+1, fresh)
                fresh = addcell(r,c-1, fresh)
            time += 1

        return time if fresh == 0 else -1