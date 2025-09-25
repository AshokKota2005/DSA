class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        list1 = []
        for i in range(0,len(matrix)):
            ele = matrix[i][:len(matrix[0])]
            list1.append(min(ele))
        list2 = []
        for i in range(0,len(matrix[0])):
            res = []
            for j in range(0,len(matrix)):
                res.append(matrix[j][i])
            list2.append(max(res))
        res = []
        for i in range(0,len(list1)):
            if list1[i] in list2:
                res.append(list1[i])
        return res
        