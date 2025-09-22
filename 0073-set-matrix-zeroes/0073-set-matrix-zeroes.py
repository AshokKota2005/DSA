class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            matrix[i] = [0] * len(matrix[0])
        for i in cols:
            for j in range(0,len(matrix)):
                matrix[j][i] = 0
            
        """
        Do not return anything, modify matrix in-place instead.
        int(matrix)"""
        