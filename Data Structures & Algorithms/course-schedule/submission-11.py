class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjacency list
        adjacency = {i:[] for i in range(numCourses)}

        #for loop .append adjacency
        for crs,prq in prerequisites:
            adjacency[crs].append(prq)

 
        visited = set()
        cycle = set()
        

        def dfs(course):
            
            if course in cycle:
       
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            visited.add(course)
            for prq in adjacency[course]:
                if dfs(prq) == False:
                    return False
            cycle.remove(course)
            
            return True
        #dfs def (course)
        #if in visited return false
        #for prq in adjacency[course]
        # visited.add(course)
        # if not dfs(prq):
        # return False
        
        #for loop dfs
        #if dfs false return false else true
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
