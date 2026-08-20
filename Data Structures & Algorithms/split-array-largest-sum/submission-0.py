class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 0    # count of possible subarrays
            curSum = 0      # iterative adder
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n  # it exceeded after adding n so it is used to start the next subarray
            return subarray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l+r)//2
            if canSplit(m):     # canSplit tells if we can split a subarray
                res = m
                r =  m - 1
            else:
                l = m + 1

        return res