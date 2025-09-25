class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        for i in range(0,len(self.grid)):
            for j in range(0,len(self.grid[0])):
                if self.grid[i][j] == value:
                    sum1 = 0
                    if 0 <= i-1 <len(self.grid) and 0 <= j < len(self.grid):
                        sum1 = sum1 + self.grid[i-1][j]
                    if 0 <= i+1 <len(self.grid) and 0 <= j < len(self.grid):
                        sum1 = sum1 + self.grid[i+1][j]
                    if 0 <= i <len(self.grid) and 0 <= j-1 < len(self.grid):
                        sum1 = sum1 + self.grid[i][j-1]
                    if 0 <= i <len(self.grid) and 0 <= j+1 < len(self.grid):
                        sum1 = sum1 + self.grid[i][j+1]
        return sum1    

    def diagonalSum(self, value: int) -> int:
        for i in range(0,len(self.grid)):
            for j in range(0,len(self.grid)):
                if self.grid[i][j] == value:
                    sum1 = 0
                    if 0 <= i-1 <len(self.grid) and 0 <= j-1 < len(self.grid):
                        sum1 = sum1 + self.grid[i-1][j-1]
                    if 0 <= i+1 <len(self.grid) and 0 <= j+1 < len(self.grid):
                        sum1 = sum1 + self.grid[i+1][j+1]
                    if 0 <= i-1 <len(self.grid) and 0 <= j+1 < len(self.grid):
                        sum1 = sum1 + self.grid[i-1][j+1]
                    if 0 <= i+1 <len(self.grid) and 0 <= j-1 < len(self.grid):
                        sum1 = sum1 + self.grid[i+1][j-1]
        return sum1
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)