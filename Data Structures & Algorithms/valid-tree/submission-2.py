class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = {i:[] for i in range(n)}

        for edge1,edge2 in edges:
            adjacency[edge1].append(edge2)
            adjacency[edge2].append(edge1)

        visited = set()
        def dfs(node,parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjacency[node]:
                if nei == parent:
                    continue
                if dfs(nei,node) == False:
                    return False
         
            return True
        
        result = dfs(0,-1)
        return True if len(visited) == n and result == True else False
        