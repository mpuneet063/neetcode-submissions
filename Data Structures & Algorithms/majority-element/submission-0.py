class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)

        for c in counts.values():
            if c > math.floor(len(nums)/2):
                return next(k for k, v in counts.items() if v==c)