class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #directed graph > dfs or bfs
        adjacency = {i:[] for i in range(numCourses)}

        for crs,prq in prerequisites:
            adjacency[crs].append(prq)
        
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False

            cycle.add(course)

            for prq in adjacency[course]:
                if not dfs(prq):
                    return False
            cycle.remove(course)
            adjacency[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True