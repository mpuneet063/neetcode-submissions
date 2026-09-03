class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import chain,combinations
        def powerset(s):
            return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

        k = list(powerset(nums))
        xor = []
        for i in k:
            r = 0
            for j in range(len(i)):
                r ^= i[j]
            xor.append(r)

        return sum(xor)