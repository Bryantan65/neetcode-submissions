class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = {i:[] for i in range(n)}

        for i,j in edges:
            adjacency[i].append(j)
            adjacency[j].append(i)
        

        visited = set()
        count = 0

        def dfs(i):
            #not sure tbh
            #loop through the 0 12, then 3-4, increase count for each situation
            visited.add(i)
            for j in adjacency[i]:
                if j not in visited:
                    dfs(j)


        
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            count+=1

        return count
    # 1. skip if already seen
    # 2. explore everything reachable from i
    # 3. that was one component