class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0
        if len(nums) == 0:
            return len(nums)
        for n in nums:
            if n == val:
                val_count += 1
        if val_count != 0:
            for v in range(val_count+1):
                nums.remove(val)
                nums.append(val)

        return len(nums) - val_count