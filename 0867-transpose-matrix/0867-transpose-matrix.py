class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        b =[]
        for i in range(n):
            col = []
            for j in range(m):
                col.append(0)
            b.append(col)
        for i in range(0,n):
            for j in range(0,m):
                b[i][j] = matrix[j][i]
        return b
            
        
        