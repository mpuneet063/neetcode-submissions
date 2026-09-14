class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        isreq = [set() for _ in range(numCourses)]

        for p, c in prerequisites:
            adj[p].add(c)
            indegree[c] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for n in adj[node]:
                isreq[n].add(node)
                isreq[n].update(isreq[node])
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return [u in isreq[v] for u, v in queries]