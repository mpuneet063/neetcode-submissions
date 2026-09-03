class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import chain, combinations
        k =  list(chain.from_iterable(combinations(nums,r) for r in range(len(nums)+1)))
        return [list(i) for i in k]