class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        memo[len(s)] = True

        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)