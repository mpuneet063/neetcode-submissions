class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)

        for src, dst in sorted(tickets)[::-1]:
            flights[src].append(dst)

        res = []

        def dfs(src):
            while flights[src]:
                dst = flights[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]
        
        