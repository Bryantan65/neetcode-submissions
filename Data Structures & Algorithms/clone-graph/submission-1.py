"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldtonew = {}
        
        def dfs(cur):
            if cur in oldtonew:
                return oldtonew[cur]
            copy = Node(cur.val)
            oldtonew[cur] = copy

            
            for nei in cur.neighbors:
                nei_copy = dfs(nei)
                copy.neighbors.append(nei_copy)
            return copy
            
        return dfs(node)
