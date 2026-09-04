class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            # decision to include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            

            # decision to not include nums[i]
            cur.pop()
            dfs(i+1, cur, total)

        cur, total = [], 0
        dfs(0, cur, total)
        return res