class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # solution using graph (optimal)
        # we need to find a vertex where 
        # num(incoming) == n-1 but num(outgoing) == 0
        incoming, outgoing = {}, {}

        for t in trust:
            if outgoing.get(t[0]):
                outgoing[t[0]] += 1
            else:
                outgoing[t[0]] = 1

            if incoming.get(t[1]):
                incoming[t[1]] += 1
            else:
                incoming[t[1]] = 1

        for i in incoming:
            if incoming[i] == n-1 and i not in outgoing:
                return i

        return -1