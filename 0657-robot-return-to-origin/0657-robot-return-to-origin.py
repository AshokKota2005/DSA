class Solution:
    def judgeCircle(self, moves: str) -> bool:
        grid = [0,0]
        for char in moves:
            if char == 'U':
                grid[1] += 1
            elif char == 'D':
                grid[1] -= 1
            elif char == 'R':
                grid[0] += 1
            elif char == 'L':
                grid[0] -= 1
        if grid[0] == 0 and grid[1] == 0:
            return True
        else:
            return False
