class Solution:
    def reorganizeString(self, s: str) -> str:
        rec = collections.Counter(s)
        counter = [(freq, char) for char, freq in rec.items()]
        heapq.heapify_max(counter)
        cooldown = deque()
        res = ''
        r, n = 0, 1
        flag = True
        while flag:
            if counter:
                f, c = heapq.heappop_max(counter)
                res += c
                r += 1
            else:
                return ''
            if f>1:
                cooldown.append([(f-1,c), r])
            
            if cooldown and r == cooldown[0][1] + n :
                heapq.heappush_max(counter, cooldown.popleft()[0])
                
            if not counter and not cooldown:
                flag = False

        return res