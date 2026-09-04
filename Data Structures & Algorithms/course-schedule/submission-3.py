class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      
        preMap = {i:[] for i in range(numCourses)}

        for prq,crs in prerequisites:
            preMap[crs].append(prq)
        
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
            if not dfs(c):
                return False
        
        return True