class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1]*(n+1) for _ in range(n)]
        def dfs(i,j):
            if i == n:
                return 0

            if memo[i][j + 1] != -1:
                return memo[i][j+1] 
            
            
            LIS = dfs(i+1, j)     # skip nums[i]
            
            if j == -1 or nums[j] < nums [i]: 
                # i.e. not increasing
                LIS = max(1 + dfs(i+1, i), LIS)
            
            memo[i][j+1] = LIS
            return LIS

        return dfs(0,-1)