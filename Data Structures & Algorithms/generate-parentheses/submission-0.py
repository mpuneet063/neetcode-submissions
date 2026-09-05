class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        left, right = 0,0
        stk = []

        def backtrack(left, right):
            if left == right == n:
                res.append(''.join(stk))

            if left < n:
                stk.append('(')
                backtrack(left+1, right)
                stk.pop()

            if right < left:
                stk.append(')')
                backtrack(left, right+1)
                stk.pop()
            
        backtrack(left, right)
        return res