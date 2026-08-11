class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0
        sums = {0:1}

        for n in nums:
            cursum += n
            diff = cursum - k

            res += sums.get(diff, 0)
            sums[cursum] = 1 + sums.get(cursum, 0)

        return res