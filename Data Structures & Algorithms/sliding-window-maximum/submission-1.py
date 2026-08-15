class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque() # collects indices
        l = r = 0

        while r < len(nums):    # running right pointer till there's nums
            while q and nums[q[-1]] < nums[r]: # remove leftmost and add new only if new is less than what is before it, i.e. monotonously decreasing queue
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()     # window has slided
            
            if (r+1) >= k:
                res.append(nums[q[0]])  # window is full, add the largest(leftmost) value to the res
                l += 1 # left is moved only when window is full
            r += 1 # move forward the right pointer

        return res
