class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(s):
            l, r = 0, len(s)-1
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def dfs(i, sub):
            if i >= len(s):
                res.append(sub.copy())
                return

            for j in range(i, len(s)):
                st = s[i:j+1]
                if isPali(st):
                    sub.append(st)
                    dfs(j+1, sub)
                    sub.pop()

        dfs(0,[])
        return res