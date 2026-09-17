class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # implement with Dijkstra
        adj = defaultdict(list)
        for t in times:
            adj[t[0]].append(t[1:])

        minHeap = [[0,k]]
        res = 0
        visit = set()

        while minHeap:
            path, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = path
            for n1, w1 in adj[node]:
                if n1 not in visit:
                    heapq.heappush(minHeap, [path+w1,n1])

        return res if len(visit) == n else -1