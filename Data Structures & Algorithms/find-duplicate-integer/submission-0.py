class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if not count.get(n):
                count[n] = 1
            else:
                count[n] += 1


        for n, _ in count.items():
            if count[n] > 1:
                return n
