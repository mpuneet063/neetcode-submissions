class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter

        counts = Counter(nums)
        cutoff = len(nums) // 3

        return [key for key, value in counts.items() if value > cutoff]