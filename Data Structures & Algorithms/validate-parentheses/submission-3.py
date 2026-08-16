class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        left = '[{('
        right = ']})'
        stk = []
        for i in s:
            if i in left:
                stk.append(i)
            else:
                if stk and stk[-1] in left:
                    if right.index(i) == left.index(stk[-1]):
                        stk.pop()
                    else:
                        stk.append(i)
                else:
                    stk.append(i)
        if stk:
            return False
        else:
            return True
