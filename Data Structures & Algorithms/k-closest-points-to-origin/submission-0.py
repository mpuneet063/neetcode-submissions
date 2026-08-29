class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        dist = []
        rec = collections.defaultdict(list)
        for p in points:
            a = p[0] - origin[0]
            b = p[1] - origin[1]
            c = math.sqrt(a**2+b**2)
            dist.append(round(c,2))
            rec[round(c,2)].append(p)

        heapq.heapify(dist)
        res = []
        while k>0:
            x = heapq.heappop(dist)
            res.append(rec[x].pop())
            k -= 1

        return res