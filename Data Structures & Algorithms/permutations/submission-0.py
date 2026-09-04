class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        res = []
        if k == 0:
            return [[]]

        perms = self.permute(nums[1:])
        for p in perms:
            for i in range(len(p) + 1):
                pc = p.copy()
                pc.insert(i,nums[0])
                res.append(pc)

        return res