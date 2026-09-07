class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = {i:[] for i in range(n)}

        for i,j in edges:
            adjacency[i].append(j)
            adjacency[j].append(i)
        
        visited = set()
        
        def dfs(i,prev):
  
            if i in visited:
                    return False
            visited.add(i)
            for j in adjacency[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            
            
            return True

        
        return dfs(0,-1) and len(visited)==n 