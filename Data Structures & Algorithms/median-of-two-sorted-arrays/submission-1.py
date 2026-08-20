class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n%2 == 1:
            m = (n+1)//2
            return nums[m-1]
        else:
            m = n//2
            o = (n//2)+1
            x = nums[m-1] + nums[o-1]
            return x/2