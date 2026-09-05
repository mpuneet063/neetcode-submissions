class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k = len(nums)
        if k == 0:
            return [[]]
        seen = set()
        res = []
        perms = self.permuteUnique(nums[1:])
        for p in perms:
            for i in range(len(p) + 1):
                pc = p.copy()
                pc.insert(i,nums[0])
                t = tuple(pc)
                if t not in seen:
                    seen.add(t)
                    res.append(pc)

        return res