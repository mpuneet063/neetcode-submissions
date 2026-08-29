class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        rec = {}
        for t in tasks:
            rec[t] = 1 + rec.get(t,0)
        counter = [(freq, task) for task, freq in rec.items()]
        heapq.heapify_max(counter)
        cooldown = deque()
        r, cycles = 0,0
        flag = True
        while flag:
            r += 1
            if counter:
                f, t = heapq.heappop_max(counter)
                if f>1:
                    cooldown.append([(f-1,t),r])
            
            if cooldown and r == cooldown[0][1] + n :
                heapq.heappush_max(counter, cooldown.popleft()[0])
                
            if not counter and not cooldown:
                flag = False

        return r