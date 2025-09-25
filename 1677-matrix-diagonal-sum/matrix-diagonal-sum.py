class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1 = 0
        list1 = []
        for i in range(0,len(mat)): 
            sum1 = sum1 + mat[i][i]
            list1.append([i,i])
        for i in range(0,len(mat)):
            j = len(mat)-i-1
            if [i,j] not in list1:
                sum1 = sum1 + mat[i][j]
        return sum1
        