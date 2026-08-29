class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for t in tasks:
            count[ord(t)-ord('A')] += 1

        maxf = max(count)
        maxCount = 0
        for c in count:
            maxCount += 1 if c == maxf else 0

        time = (maxf-1)*(n+1) + maxCount
        return max(len(tasks), time)