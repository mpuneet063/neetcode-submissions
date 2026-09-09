class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {len(s):0}
        def back(i):
            if i in dp:
                return dp[i]

            res = 1 + back(i+1)
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in words:
                    res = min(res, back(j+1))
            dp[i] = res
            return res

        return back(0)
        