class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minh = [[grid[0][0], 0,0]]     # [max-height, r, c]
        direc = [[0,1], [0,-1], [1,0], [-1,0]]
        visit.add((0,0))
        while minh :
            t, r, c = heapq.heappop(minh)
            visit.add((r,c))
            if r == n-1 and c == n - 1:
                return t
            for dx, dy in direc:
                nr, nc = r + dx, c + dy
                if (nr < 0 or nc < 0 or 
                    nr == n or nc == n or (nr,nc) in visit):
                    continue
                visit.add((nr,nc))
                heapq.heappush(minh, [max(t,grid[nr][nc]), nr, nc])