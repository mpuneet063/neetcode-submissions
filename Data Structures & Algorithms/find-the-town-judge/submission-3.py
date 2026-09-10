class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(list)
        ppl = []
        for t in trust:
            trust_map[t[0]].append(t[1])
            ppl.extend(t)
        trusted = list(trust_map.values())

        ppl = list(set(ppl))
        for p in ppl:
            if p not in trust_map:
                flag = True
                for t in trusted:
                    if p not in t:
                        flag = False
                if flag:
                    return p
        return -1