class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        list1 = []
        i = 1
        temp = 0
        while i not in list1:
            list1.append(i)
            temp += 1
            for j in range(1,(temp*k)+1):
                if i == n:
                    i = 1
                else:
                    i += 1
        res = []
        for i in range(1,n+1):
            if i not in list1:
                res.append(i)
        return res
        