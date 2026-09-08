class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        cur = []
        words = set(wordDict)

        def back(i):
            if i == len(s):
                copy = " ".join(cur)
                res.append(copy)
                return
            
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in words:
                    cur.append(w)
                    back(j+1)
                    cur.pop()
                    

            
        back(0)
        return res