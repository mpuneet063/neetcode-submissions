class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        turns = 0
        if '0000' in deadends:
            return -1
        
        q = deque([('0000', 0)])
        visit = set()
        visit.add('0000')
        for d in deadends:
            visit.add(d)
        def child(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        while q:
            comb, turn = q.popleft()
            if comb == target:
                return turn
                
            for c in child(comb):
                if c not in visit:    
                    visit.add(c)
                    q.append((c, turn+1))
        return -1