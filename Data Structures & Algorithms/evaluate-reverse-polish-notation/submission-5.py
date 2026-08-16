class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        stk = []
        for t in tokens:
            if t == '+':
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)
            elif t == '-':
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif t == '*':
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)
            elif t == '/':
                a = stk.pop()
                b = stk.pop()
                if a != 0:    
                    stk.append(int(b/a))
            else:
                stk.append(int(t))

        return stk[-1]