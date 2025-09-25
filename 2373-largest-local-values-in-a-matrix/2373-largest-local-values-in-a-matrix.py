class Solution(object):
    def largestLocal(self, grid):
        result = []
        for i in range(0,len(grid)-2):
            list1 = [0] * (len(grid)-2)        
            result.append(list1)
        i = 0
        while i < len(result):
            j = 0
            while j < len(result[0]):
                max1 = 0
                for k in range(i,i+3):
                    for s in range(j,j+3):
                        if grid[k][s] > max1:
                            max1 = grid[k][s]
                result[i][j] = max1 
                j = j+1
                print('k')
            i = i+1
        return result