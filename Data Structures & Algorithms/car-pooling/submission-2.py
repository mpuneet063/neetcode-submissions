class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fro, to = defaultdict(list), defaultdict(list)
        points = []
        for t in trips:
            if t[1] not in points:
                points.append(t[1])
            if t[2] not in points:
                points.append(t[2])
            fro[t[1]].append(t[0])
            to[t[2]].append(t[0])
        points.sort()
        # print(points)
        occ = 0
        flag = True
        while points:
            loc = points.pop(0)
            # print(loc, occ)
            if loc in to:
                occ -= sum(to[loc])
            if loc in fro:
                if occ + sum(fro[loc]) <= capacity:
                    occ += sum(fro[loc])
                else:
                    flag = False
                    break
        return flag