class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        cycle, visit = set(), set()

        def dfs(crs, res):
            if crs in cycle:
                # Cycle detected
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre, res):
                    return False
                # res.append(pre)
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        res = []
        for c in range(numCourses):
            if not dfs(c,res):
                return []
        return res 
        