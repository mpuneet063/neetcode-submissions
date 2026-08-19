import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def days_taken(k):
            ships = 1
            curr = k
            for w in weights:
                if curr -w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr = k
                curr -= w
            return True

        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            m = (l+r)//2

            if days_taken(m):
                res = min(res,m)
                r = m - 1
            else: 
                l = m + 1
                

        return res