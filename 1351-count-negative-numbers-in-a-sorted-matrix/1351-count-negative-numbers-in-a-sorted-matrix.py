class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] < 0:
                    c = c+1  
        return c