class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        subset = []
        def dfs(j):
            if len(subset) == k:
                res.append(subset.copy())
                # print(res,subset)
                return
            for i in range(j, len(nums)):
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                # dfs(i+1)

        dfs(0)
        return res