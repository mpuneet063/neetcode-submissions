class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        return heapq.nlargest(self.k, self.nums)[-1]
        if len(self.nums) < self.k:
            return self.nums[0]
        else:
            return self.nums[-self.k]
