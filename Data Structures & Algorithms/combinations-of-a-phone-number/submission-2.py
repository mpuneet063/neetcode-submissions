class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digichar = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno',
                    '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        if not digits:
            return [] 
        def dfs(i, sub):
            if i == len(digits):
                if len(sub) == len(digits):
                    res.append(''.join(sub.copy()))
                    return
                else:
                    return
            
            for j in range(i,len(digits)):
                for k in digichar[digits[j]]:
                    sub.append(k)
                    dfs(j+1, sub)
                    sub.pop()

        dfs(0,[])
        return res