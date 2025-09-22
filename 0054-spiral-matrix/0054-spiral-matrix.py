class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left,top = 0,0
        right,bottom = len(matrix[0]),len(matrix)
        limit = len(matrix[0]) * len(matrix)
        j = 1
        while j <= limit:
            if j <= limit:
                for i in range(left,right):
                    res.append(matrix[top][i])
                    j += 1
                top += 1
            if j <= limit:
                for i in range(top,bottom):
                    res.append(matrix[i][right-1])
                    j += 1
                right -= 1
            if j <= limit:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[bottom-1][i])
                    j += 1
                bottom -= 1
            if j <= limit:
                for i in range(bottom-1,top-1,-1):
                    res.append(matrix[i][left])
                    j += 1
                left += 1
        return res

        