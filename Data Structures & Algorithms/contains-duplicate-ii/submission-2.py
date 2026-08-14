class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = {}
        for i , n in enumerate(nums):
            if n in idx:
                if i - idx[n] <= k:
                    return True
            idx[n] = i
    

        return False