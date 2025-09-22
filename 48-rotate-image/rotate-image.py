class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(0,len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        length = len(matrix[0])
        for i in range(length):
            for j in range(0,length//2):
                matrix[i][j],matrix[i][length-1-j] = matrix[i][length-1-j],matrix[i][j]