class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        minHeap = [[0,0,0]]  # [diff, r, c]

        visit = set()

        direc = [[0,1], [0,-1], [1,0], [-1,0]]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            
            visit.add((r,c))
            if (r,c) == (rows - 1, cols - 1):
                return diff

            for dr, dc in direc:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or
                    nr == rows or nc == cols or (nr,nc) in visit):
                    continue
                d = max(abs(heights[r][c] - heights[nr][nc]), diff)
                heapq.heappush(minHeap, [d, nr,nc])