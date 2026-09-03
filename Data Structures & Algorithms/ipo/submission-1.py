class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital) and k >= len(capital):
            return sum(profits) + w
        maxProfit = []
        minCap = [(c,p)for c, p in zip(capital, profits)]
        heapq.heapify(minCap)

        for i in range(k):
            while minCap and minCap[0][0] <= w:
                _, p = heapq.heappop(minCap)
                heapq.heappush_max(maxProfit, p)
            if not maxProfit:
                break
            w += heapq.heappop_max(maxProfit)

        return w