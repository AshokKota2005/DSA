class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(0,n):
            col = [0] * n
            matrix.append(col)
        left,top = 0,0
        right,bottom = n,n
        j = 1
        limit = n*n
        while j <= limit:
            if j <= limit:
                for i in range(left,right):
                    matrix[top][i] = j
                    j += 1
                top += 1
                print(matrix)
            if j <= limit:
                for i in range(top,bottom):
                    matrix[i][right-1] = j
                    j += 1
                right -= 1
                print(matrix)
            if j <= limit:
                for i in range(right-1,left-1,-1):
                    matrix[bottom-1][i] = j
                    j += 1
                bottom -= 1
                print(matrix)
            if j <= limit:
                for i in range(bottom-1,top-1,-1):
                    matrix[i][left] = j
                    j += 1
                left += 1
                print(matrix)
        return matrix

        