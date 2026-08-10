class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def getRegion(matrix, row1, col1, row2, col2):
            submatrix = []
            for r in range(row1, row2+1):
                curr_row = matrix[r]
                submatrix.append(curr_row[col1:col2+1])

            return submatrix

        import numpy as np
        submatrix = getRegion(self.matrix, row1, col1, row2, col2)

        return np.sum(submatrix)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)