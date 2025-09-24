class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list1 = list(str(n))
        list1 = list(map(int,list1))
        print(list1)
        res = 1
        sum1 = 0
        for i in range(len(list1)):
            sum1 = sum1 + list1[i]
            res = res * list1[i] 
        return res - sum1
            
        