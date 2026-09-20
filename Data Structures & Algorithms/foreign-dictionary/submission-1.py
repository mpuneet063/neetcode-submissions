class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # solve with Topological sort
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # have same prefix
                return ''
            
            for j in range(minLen):
                # find first diff char
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    # store first diff in set

        visit = {}  # False = visited, True = current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res = res[::-1]
        print(res)
        return ''.join(res)
