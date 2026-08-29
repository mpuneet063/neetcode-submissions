class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        while k>1:
            heapq.heappop_max(nums)
            k -= 1

        return nums[0]