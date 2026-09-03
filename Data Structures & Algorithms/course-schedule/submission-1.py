class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)
        #WHY KAIBAO NO GOLD GOLD GOLD
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for prq in preMap[course]:
                if dfs(prq) == False:
                    return False
            preMap[course] = []
            visited.remove(course)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return False

        return True
