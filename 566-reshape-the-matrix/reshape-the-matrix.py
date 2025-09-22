class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        original = []
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                original.append(mat[i][j])
        if r*c == len(original):
            i,j = 0,0
            res = []
            while j<r:
                list1 = []
                while i < len(original):
                    if len(list1) < c:
                        list1.append(original[i])
                        i = i+1
                    else:
                        break
                res.append(list1)
                j = j+1
            return res
        else:
            return mat
        
        