class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        must = {i: [] for i in range(numCourses)}
        if not prerequisites:
            return True
        for c,p in prerequisites:
            must[c].append(p)

        visiting = set()
        def dfs(course):
            if course in visiting:
                # cycle detected
                return False
            if must[course] == []:
                return True

            visiting.add(course)
            for pre in must[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            must[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True