class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:
                    count += 4
                    if 0 <= i-1 < len(grid):
                        if grid[i-1][j] == 1:
                            count -= 1
                    if 0 <= i+1 < len(grid):
                        if grid[i+1][j] == 1:
                            count -= 1
                    if 0 <= j-1 < len(grid[0]):
                        if grid[i][j-1] == 1:
                            count -= 1
                    if 0 <= j+1 < len(grid[0]):
                        if grid[i][j+1] == 1:
                            count -= 1
                print(count)
        return count
                     
