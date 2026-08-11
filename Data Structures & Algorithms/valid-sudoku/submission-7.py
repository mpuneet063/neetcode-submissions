class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def duplicate(l):
            valuelist = [i for i in l if i!= '.']
            if len(valuelist) != len(set(valuelist)):
                return True
            else:
                return False
        
        for row in board:
            if duplicate(row):
                return False
        
        import numpy as np
        board_t = np.array(board).transpose().tolist()

        for col in board_t:
            if duplicate(col):
                return False

        np_board = np.array(board)

        blocks = [
            np_board[i:i+3, j:j+3]
            for i in range(0,9,3)
            for j in range(0,9,3)
        ]
        
        for b in blocks:
            if duplicate(b.flatten().tolist()):
                return False

        return True