class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                # print(res,subset)
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return [res[i] for i in range(len(res)) if len(res[i])==k]