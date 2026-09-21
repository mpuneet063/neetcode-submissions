class Solution:
    def climbStairs(self, n: int) -> int:
        # DP (bottom-up)
        dp = [1]
        for i in range(n):
            if len(dp) < 2:
                dp.append(1)
            else:
                dp.append(dp[-1]+dp[-2])
        return dp[-1]