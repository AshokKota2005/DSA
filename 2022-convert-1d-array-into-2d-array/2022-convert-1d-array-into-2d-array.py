class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n == len(original):
            i,j = 0,0
            res = []
            while j<m:
                list1 = []
                while i < len(original):
                    if len(list1) < n:
                        list1.append(original[i])
                        i = i+1
                    else:
                        break
                res.append(list1)
                j = j+1
            return res
        else:
            return []
        