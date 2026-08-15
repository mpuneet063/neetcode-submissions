class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for a in arr:
            diff.append((abs(x-a), a))

        diff.sort()

        return sorted([v for d,v in diff[:k]])