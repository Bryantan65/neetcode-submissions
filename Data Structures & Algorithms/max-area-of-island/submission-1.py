class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        visited = set()
        best = 0

        def dfs(r,c):
            if r < 0 or r >= row or c <0 or c>=col or (r,c) in visited or grid[r][c] == 0:
                return False
            
            visited.add((r,c))

            return 1+ dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    best = max(dfs(r,c),best)
                    
        return best
                    
