class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        from itertools import chain , combinations
        comb = (list(chain.from_iterable(combinations(nums,k))))
        return [comb[i:i+k] for i in range(0, len(comb), k)]