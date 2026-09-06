class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        
        adjacency = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in adjacency[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n
