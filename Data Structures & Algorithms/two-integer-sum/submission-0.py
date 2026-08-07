class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = []
        for i, j in enumerate(nums):
            for n, m in enumerate(nums):
                if j+m == target and i!=n:
                    k.append(i)
                    k.append(n)

        return list(set(k))