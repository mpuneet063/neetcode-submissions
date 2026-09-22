class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            tmp = [nums[i]]
            for j in range(i+2,len(dp)):
                tmp.append(nums[i]+dp[j])
            dp[i] = max(tmp)
        return max(dp)