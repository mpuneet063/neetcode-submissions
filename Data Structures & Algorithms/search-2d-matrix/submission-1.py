class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = []
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                targetRow = row
                break
        
        # l, r = 0, len(targetRow) - 1

        # while l <= r:
        #     m = l + (r-1)//2

        #     if target < targetRow[m]:
        #         l = m + 1
        #     elif target > targetRow[m]:
        #         r = m - 1
        #     else:
        #         return True

        flag = False
        if target in targetRow:
            flag = True
        return flag