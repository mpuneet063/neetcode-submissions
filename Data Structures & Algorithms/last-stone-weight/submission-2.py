class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            heapq.heapify_max(stones)
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print(x,y)
            if x == y:
                continue
            elif x < y:
                heapq.heappush_max(stones, (y-x))
            else:
                heapq.heappush_max(stones, (x-y))

        return stones[0] if stones else 0