class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r and grid[r-1][c]:  # if top is land
                        perimeter -= 2
                    if c and grid[r][c-1]:  # if left is land
                        perimeter -= 2


        return perimeter