class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        preMap = {i:[] for i in range(numCourses)}

        for crs, prq in prerequisites:
            preMap[crs].append(prq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False #this is the cycle detection
            if preMap[course] == []:
                return True
            visited.add(course)
            for prq in preMap[course]:
                #if my previous step was False (meaning there's a cycle)
                #return False
                if not dfs(prq):
                    return False
            preMap[course] = []
            visited.remove(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
