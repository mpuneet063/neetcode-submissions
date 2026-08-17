class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        stk = []
        for t in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[t]:
                # print(stk)
                res[stk[-1]] = t - stk[-1]
                stk.pop()
                # print(res)
            stk.append(t) 
            # print(stk)

        return res