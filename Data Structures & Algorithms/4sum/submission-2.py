class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, len(nums) - 1
                while l<r:
                    foursum = a + nums[j] + nums[l] + nums[r]
                    if foursum > target:
                        r -= 1
                    elif foursum < target:
                        l += 1
                    else:
                        res.append([a, nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
        if len(res) > 1 and res[0] == res[1]:
            return [res.pop()]
        return res