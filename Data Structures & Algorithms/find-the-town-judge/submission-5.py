class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # solution using graph (optimal)
        # we need to find a vertex where 
        # num(incoming) == n-1 but num(outgoing) == 0
        # NEETCODE SOLUTION
        incoming, outgoing = defaultdict(int), defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1

        for i in incoming:
            if incoming[i] == n-1 and i not in outgoing:
                return i

        return -1