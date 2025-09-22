class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list1 = []
        for i in range(0,numRows):
            if i == 0:
                ele = [i+1]
            elif i == 1:
                ele = [i,i]
            else:
                res = list1[-1]
                ele = [1]
                for i in range(0,len(res)-1):
                    a = res[i] + res[i+1]
                    ele.append(a)
                ele.append(1)
            list1.append(ele)
        return list1