class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if 0 <= i+1 < len(grid) and 0 <= j < len(grid[0]):
                    if grid[i][j]!= grid[i+1][j]:
                        return False
                if 0 <= i <= len(grid) and 0 <= j+1 < len(grid[0]):
                    if grid[i][j] == grid[i][j+1]:
                        return False
        return True        