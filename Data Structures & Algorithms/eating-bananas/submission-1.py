class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def hours_taken(k):
            h_taken = 0
            for p in piles:
                h_taken += math.ceil(p/k)
            return h_taken

        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = l + (r-l)//2
            h_taken = hours_taken(m)
            if h_taken > h:
                l = m+ 1
            else:
                k = m
                r = m - 1
        return k