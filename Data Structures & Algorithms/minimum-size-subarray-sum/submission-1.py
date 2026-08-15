class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if sum(nums) < target:
            return 0
        l, r, total, k = 0, 0, 0, float('inf')
        while r < len(nums)+1:
            sub = nums[l:r]
            if sum(sub) < target:
                r += 1
            else:
                k = min(len(sub), k)
                l += 1

        return k