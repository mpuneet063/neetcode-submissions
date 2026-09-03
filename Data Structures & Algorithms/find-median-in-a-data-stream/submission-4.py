class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        heapq.heapify(self.large)
        heapq.heapify_max(self.small)
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        # make sure that every element in small <= large
        if self.small and self.large and self.small[0] > self.large[0]:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        
        # uneven size?
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, heapq.heappop_max(self.small))
        
        if len(self.large) > len(self.small) + 1:
            heapq.heappush_max(self.small, heapq.heappop(self.large))

        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (self.small[0]+self.large[0])/2