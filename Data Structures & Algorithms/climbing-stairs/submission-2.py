class Solution:
    def climbStairs(self, n: int) -> int:
        q = deque([1])
        for i in range(n):
            if len(q) < 2:
                q.append(1)
            else:
                q.append(sum(q))
                q.popleft()

        return q[-1]